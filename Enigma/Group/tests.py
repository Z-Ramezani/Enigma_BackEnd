
from asyncio.windows_events import NULL
from tokenize import group
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from Group.models import Group, Members
from Group.serializers import GroupSerializer
from MyUser.models import MyUser
from unittest import mock
from unittest.mock import patch

class ShowGroupsTestCase(APITestCase):
    
    def setUp(self):
        self.user = MyUser.objects.create(email='testuser@test.local', password='testpass',  name='test', picture_id=4)

    def test_show_groups_success(self):
        self.client.force_authenticate(user=self.user)
        group = Group.objects.create(name='Test Group', currency='USD')
        Members.objects.create(userID=self.user, groupID=group)
        response = self.client.post('/group/ShowGroups/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['groups'], [{'id': group.id, 'name': group.name, 'currency': group.currency}])

    def test_show_groups_no_groups(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/group/ShowGroups/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'Error': 'User does not belong to any groups'})
   
    def test_show_groups_unauthenticated(self):
        response = self.client.post('/group/ShowGroups/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_show_groups_invalid_method(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/group/ShowGroups/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_show_groups_exception(self):
        self.client.force_authenticate(user=self.user)
        with mock.patch('Group.views.Members.objects.filter') as mock_filter:
            mock_filter.side_effect = Exception('test exception')
            response = self.client.post('/group/ShowGroups/')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data, {'Error': 'test exception'})


class DeleteGroupTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = MyUser.objects.create(email='testuser@test.local', password='testpass',  name='test', picture_id=4)
        self.client.force_authenticate(user=self.user)
        self.group = Group.objects.create(name='Test Group')

    def test_delete_group_success(self):
        Members.objects.create(userID=self.user, groupID=self.group)
        data = {'groupID': self.group.id}
        response = self.client.post("/group/DeleteGroup/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Group deleted successfully.'})
   

    @patch('Group.views.IsGroupUser.has_permission')
    def test_delete_group_not_found(self,mock_has_permission):
        mock_has_permission.return_value = True
        data = {'groupID': 9999} # invalid group ID
        response = self.client.post("/group/DeleteGroup/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Group not found.'})
        self.assertTrue(Group.objects.filter(id=self.group.id).exists())

    def test_delete_group_unauthorized(self):
        data = {'groupID': self.group.id}
        response = self.client.post("/group/DeleteGroup/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_with_exception(self):
        data = {'groupID': self.group.id}
        with mock.patch('Group.models.Group.objects.get') as mock_get:
            mock_get.side_effect = Exception('Something went wrong')
            response = self.client.post('/group/GroupInfo/', data)
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class GroupInfoTest(APITestCase):
    def setUp(self):
        self.user1 = MyUser.objects.create(email='maryam@test.local', name='maryam', password='maryam', picture_id=2)
        self.client = APIClient()
        self.group = Group.objects.create(name='Test Group', description= "Family", currency="تومان", picture_id=2)
        self.valid_payload = {'groupID': self.group.id}
        self.invalid_payload = {'groupID': 999}

    def test_post_with_valid_payload(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post('/group/GroupInfo/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = GroupSerializer(self.group)
        self.assertEqual(response.data, serializer.data)
    
    def test_post_with_invalid_payload(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post('/group/GroupInfo/', self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Group not found.'})


    def test_post_without_authentication(self):
        response = self.client.post('/group/GroupInfo/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_with_exception(self):
        self.client.force_authenticate(user=self.user1)
        with mock.patch('Group.models.Group.objects.get') as mock_get:
            mock_get.side_effect = Exception('Something went wrong')
            response = self.client.post('/group/GroupInfo/', self.valid_payload)
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def test_post_without_group_id(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post('/group/GroupInfo/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message': 'Group not found.'})