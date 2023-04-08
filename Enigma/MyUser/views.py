from django.shortcuts import render
from .models import MyUser

from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from .serializers import MyUserSerializer, ChangePasswordSerializer

class RegisterUsers(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MyUserSerializer

class ChangePasswordView(generics.UpdateAPIView):

    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer