from django.shortcuts import render
from .models import MyUser
from .serializers import MyUserSerializer, UpdateUserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView

class RegisterUsers(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MyUserSerializer

class EditProfile(UpdateAPIView):
    
    users = MyUser.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    # def put(self, request, pk):
    #     user = MyUser.objects.filter(pk = pk)
    #     self.check_object_permissions(request, user)
    #     print(user)
    #     print("------------------------------------------------------------------------")
    #     edit_profile = {}
    #     edit_profile['username'] = user.username
    #     edit_profile['password'] = user.password
    #     edit_profile['picture_id'] = user.picture_id


