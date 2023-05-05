from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from MyUser.models import MyUser

class RegisterAndAuthenticateTest(APITestCase):

    def authenticate(self):
        user_info = {
        "email":"u@u.com",
        "password":123 ,
        "name":"Uali",
        "picture_id" :10}
        
        self.client.post(('/auth/register/'),user_info)
        response = self.client.post(('/auth/token/'), {"username":"u@u.com",
                                                       "password":123})

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_should_not_register_invalid_email(self):
        user_info = {
        "email":"uu.com",
        "password":123 ,
        "name":"Uali",
        "picture_id" :10}
        
        response = self.client.post(('/auth/register/'),user_info)
        self.assertEqual(response.status_code, 400)
        
    def test_should_not_register_invalid_password(self):
        user_info = {
        "email":"uu.com",
        "password":"",
        "name":"Uali",
        "picture_id" :10}
        
        response = self.client.post(('/auth/register/'),user_info)
        self.assertEqual(response.status_code, 400)

    def test_should_register(self):
        user_info = {
        "email":"u@u.com",
        "password":"usER!@123",
        "name":"Uali",
        "picture_id" :10}
        
        response = self.client.post(('/auth/register/'),user_info)
        self.assertEqual(response.status_code, 201)


    def test_should_get_token(self):
        user_info = {
        "username":"u@u.com",
        "password":"usER!@123"}
        
        self.client.post(('/auth/register/'),user_info)
        response = self.client.post(('/auth/token/'), {"username":"u@u.com",
                                                       "password":'usER!@123'})

        self.assertEqual(response.status_code, 200)

    def test_should_not_get_token_invalid_username(self):
        user_info = {
        "username":"u@u.com",
        "password":"usER!@123"}
        
        self.client.post(('/auth/register/'),user_info)
        response = self.client.post(('/auth/token/'), {"username":"u@a.com",
                                                       "password":'usER!@123'})
        self.assertEqual(response.status_code, 400)

    def test_should_not_get_token_invalid_password(self):
        user_info = {
        "username":"u@u.com",
        "password":"usER!@123"}
        
        self.client.post(('/auth/register/'),user_info)
        response = self.client.post(('/auth/token/'), {"username":"u@u.com",
                                                       "password":'usER!@12'})
        self.assertEqual(response.status_code, 400)

