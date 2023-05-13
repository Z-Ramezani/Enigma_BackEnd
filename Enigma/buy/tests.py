from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from Group.models import Group, Members
from MyUser.models import MyUser
from unittest import mock

class CreateBuyViewTest(APITestCase):
    def setUp(self):
        self.user1 = MyUser.objects.create(email='maryam@test.local', name='maryam', password='maryam', picture_id=2)
        self.user2 = MyUser.objects.create(email='maryam2@test.local', name='maryam2', password='maryam2', picture_id=3)
        self.user3 = MyUser.objects.create(email='maryam3@test.local', name='maryam3', password='maryam3', picture_id=4)
        self.client = APIClient()
        self.group = Group.objects.create(name='Test Group', description="Family", currency="تومان", picture_id=2)
        Members.objects.create(userID=self.user1, groupID=self.group)
        Members.objects.create(userID=self.user2, groupID=self.group)
        Members.objects.create(userID=self.user3, groupID=self.group)
        self.valid_payload = {
            'groupID': self.group.id,
            'description': "2 pizza",
            'cost': 200000,
            'date': '2023-5-13',
            'added_by': self.user1.user_id,
            'picture_id': 5,
            'buyers': [{
                'userID': self.user2.user_id,
                'percent': 200000
            }],
            'consumers': [
                {'userID': self.user3.user_id, "percent": 100000},
                {'userID': self.user2.user_id, "percent": 100000}
            ]
        }
        print(self.valid_payload)
        self.invalid_payload = {'groupID': 999}

    def test_create_buy_with_valid_payload(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post('/buy/CreateBuyView/', self.valid_payload)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['groupID'], self.valid_payload['groupID'])
        self.assertEqual(response.data['description'], self.valid_payload['description'])
        self.assertEqual(response.data['cost'], self.valid_payload['cost'])
        self.assertEqual(response.data['added_by'], self.valid_payload['added_by'])
