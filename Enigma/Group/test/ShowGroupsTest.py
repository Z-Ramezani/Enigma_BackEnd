
from rest_framework.test import APITestCase
from rest_framework import status
from Group.models import Group, Members
from MyUser.models import MyUser
from unittest import mock


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
