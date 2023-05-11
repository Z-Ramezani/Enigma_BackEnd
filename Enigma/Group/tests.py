
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from Group.models import Group
from Group.serializers import GroupSerializer
from MyUser.models import MyUser
from unittest import mock


class GroupTest(APITestCase):
    def setUp(self):
        self.user1 = MyUser.objects.create(email='maryam@test.local', name='maryam', password='maryam', picture_id=2)
        self.user2 = MyUser.objects.create(email='zahra@test.local', name='zahra', password='zahra', picture_id=1)
        self.user3 = MyUser.objects.create(email='fateme@test.local', name='fateme', password='fateme', picture_id=3)
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