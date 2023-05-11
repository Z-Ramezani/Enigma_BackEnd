from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from Group.models import Group, Members
from MyUser.models import MyUser
from unittest import mock
from unittest.mock import patch

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
    