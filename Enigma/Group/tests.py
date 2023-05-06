from rest_framework.test import APITestCase
from rest_framework import status

from Group.models import Group
from MyUser.models import MyUser


class GroupTest(APITestCase):
    def test_create_group_correct(self):
        user = MyUser.objects.get(id=1)
        
        response = self.client.post(
            'http://127.0.0.1:8000/group/CreateGroup/', {
                "name": "University Friends",
                "description": "Zahra Nourieh Maryam",
                "currency": "Dollar",
                "picture_id": 1,
                "emails": [
                    "maryam.shafizadegan.8098@gmail.com",
                    "miss_ramazani@yahoo.com",
                    "nourieh110@gmail.com"
                    ]
            }, format='json'
        )
        data = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual('University Friends', data['name'])
        self.assertEqual('Zahra Nourieh Maryam', data['description'])
        self.assertEqual('Dollar', data['currency'])
        self.assertEqual(1, data['picture_id'])
        self.assertEqual(1, data['creator']['id'])
        self.assertEqual('mehdi', data['creator']['username'])
        self.assertEqual(3, len(data['emails']))
        self.assertEqual('maryam.shafizadegan.8098@gmail.com', data['emails'][0])
        self.assertEqual('miss_ramazani@yahoo.com', data['emails'][1])
        self.assertEqual('nourieh110@gmail.com', data['emails'][2])

        # self.assertTrue(data['is_public'])
        # self.assertTrue(data['is_commentable'])
        # self.assertTrue(data['is_vote_retractable'])
        # self.assertEqual('', data['attached_http_link'])

    def test_create_group_name_is_null(self):
            user = MyUser.objects.get(id=1)
            
            response = self.client.post(
                'http://127.0.0.1:8000/group/CreateGroup/', {
                    "name": "",
                    "description": "Zahra Nourieh Maryam",
                    "currency": "Dollar",
                    "picture_id": 1,
                    "emails": [
                        "maryam.shafizadegan.8098@gmail.com",
                        "miss_ramazani@yahoo.com",
                        "nourieh110@gmail"
                        ]
                }, format='json'
            )
            data = response.data

            self.assertEqual(status.HTTP_201_CREATED, response.status_code)
            self.assertEqual('University Friends', data['name'])

    def test_create_group_name_is_space(self):
            user = MyUser.objects.get(id=1)
            
            response = self.client.post(
                'http://127.0.0.1:8000/group/CreateGroup/', {
                    "name": "    ",
                    "description": "Zahra Nourieh Maryam",
                    "currency": "Dollar",
                    "picture_id": 1,
                    "emails": [
                        "maryam.shafizadegan.8098@gmail.com",
                        "miss_ramazani@yahoo.com",
                        "nourieh110@gmail"
                        ]
                }, format='json'
            )
            data = response.data

            self.assertEqual(status.HTTP_201_CREATED, response.status_code)
            self.assertEqual('University Friends', data['name'])

    def test_create_group_description_is_null(self):
            user = MyUser.objects.get(id=1)
            
            response = self.client.post(
                'http://127.0.0.1:8000/group/CreateGroup/', {
                    "name": "",
                    "description": "Zahra Nourieh Maryam",
                    "currency": "Dollar",
                    "picture_id": 1,
                    "emails": [
                        "maryam.shafizadegan.8098@gmail.com",
                        "miss_ramazani@yahoo.com",
                        "nourieh110@gmail"
                        ]
                }, format='json'
            )
            data = response.data

            self.assertEqual(status.HTTP_201_CREATED, response.status_code)
            self.assertEqual('Zahra Nourieh Maryam', data['description'])

    def test_create_group_currency_is_null(self):
            user = MyUser.objects.get(id=1)
            
            response = self.client.post(
                'http://127.0.0.1:8000/group/CreateGroup/', {
                    "name": "",
                    "description": "Zahra Nourieh Maryam",
                    "currency": "Dollar",
                    "picture_id": 1,
                    "emails": [
                        "maryam.shafizadegan.8098@gmail.com",
                        "miss_ramazani@yahoo.com",
                        "nourieh110@gmail"
                        ]
                }, format='json'
            )
            data = response.data

            self.assertEqual(status.HTTP_201_CREATED, response.status_code)
            self.assertEqual('Dollar', data['currency'])

    def test_create_group_pictureID_is_zero(self):
            user = MyUser.objects.get(id=1)
            
            response = self.client.post(
                'http://127.0.0.1:8000/group/CreateGroup/', {
                    "name": "",
                    "description": "Zahra Nourieh Maryam",
                    "currency": "Dollar",
                    "picture_id": 0,
                    "emails": [
                        "maryam.shafizadegan.8098@gmail.com",
                        "miss_ramazani@yahoo.com",
                        "nourieh110@gmail"
                        ]
                }, format='json'
            )
            data = response.data

            self.assertEqual(status.HTTP_201_CREATED, response.status_code)
            self.assertEqual(1, data['picture_id'])
    
    def test_create_group_pictureID_is_nagative(self):
            user = MyUser.objects.get(id=1)
            
            response = self.client.post(
                'http://127.0.0.1:8000/group/CreateGroup/', {
                    "name": "",
                    "description": "Zahra Nourieh Maryam",
                    "currency": "Dollar",
                    "picture_id": -2,
                    "emails": [
                        "maryam.shafizadegan.8098@gmail.com",
                        "miss_ramazani@yahoo.com",
                        "nourieh110@gmail"
                        ]
                }, format='json'
            )
            data = response.data

            self.assertEqual(status.HTTP_201_CREATED, response.status_code)
            self.assertEqual(1, data['picture_id'])

    def test_create_group_pictureID_is_more_than_values(self):
        user = MyUser.objects.get(id=1)
        
        response = self.client.post(
            'http://127.0.0.1:8000/group/CreateGroup/', {
                "name": "",
                "description": "Zahra Nourieh Maryam",
                "currency": "Dollar",
                "picture_id": 100,
                "emails": [
                    "maryam.shafizadegan.8098@gmail.com",
                    "miss_ramazani@yahoo.com",
                    "nourieh110@gmail"
                    ]
            }, format='json'
        )
        data = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, data['picture_id'])

    def test_create_group_not_email(self):
        user = MyUser.objects.get(id=1)
        
        response = self.client.post(
            'http://127.0.0.1:8000/group/CreateGroup/', {
                "name": "University Friends",
                "description": "Zahra Nourieh Maryam",
                "currency": "Dollar",
                "picture_id": 1,
                "emails": [
                    ]
            }, format='json'
        )
        data = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(0, len(data['emails']))
    
    def test_create_group_invalid_email(self):
        user = MyUser.objects.get(id=1)
        
        response = self.client.post(
            'http://127.0.0.1:8000/group/CreateGroup/', {
                "name": "University Friends",
                "description": "Zahra Nourieh Maryam",
                "currency": "Dollar",
                "picture_id": 1,
                "emails": [
                    "maryam.shafizadegan.8098@gmail.com",
                    "miss_ramazani@yahoo.com",
                    "nourieh110@gmail"
                    ]
            }, format='json'
        )
        data = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, len(data['emails']))
        self.assertEqual('maryam.shafizadegan.8098@gmail.com', data['emails'][0])
        self.assertEqual('miss_ramazani@yahoo.com', data['emails'][1])
        self.assertEqual('nourieh110@gmail.com', data['emails'][2])
    

    def test_create_group_valid_email_but_is_not_register(self):
        user = MyUser.objects.get(id=1)
        
        response = self.client.post(
            'http://127.0.0.1:8000/group/CreateGroup/', {
                "name": "University Friends",
                "description": "Zahra Nourieh Maryam",
                "currency": "Dollar",
                "picture_id": 1,
                "emails": [
                    "maryam.shafizadegan.8098@gmail.com",
                    "miss_ramazani@yahoo.com",
                    "ab@gmail.com"
                    ]
            }, format='json'
        )
        data = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, len(data['emails']))
        self.assertEqual('maryam.shafizadegan.8098@gmail.com', data['emails'][0])
        self.assertEqual('miss_ramazani@yahoo.com', data['emails'][1])
        self.assertEqual('nourieh110@gmail.com', data['emails'][2])

    