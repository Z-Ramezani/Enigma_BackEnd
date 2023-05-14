from django.shortcuts import render
from .models import MyUser
from .serializers import MyUserSerializer, UpdateUserSerializer, ChangePasswordSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class RegisterUsers(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MyUserSerializer

"""
class ChangePasswordView(generics.UpdateAPIView):

    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
"""

class EditProfile(UpdateAPIView):
    
    users = MyUser.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    

class UserInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            
            user = self.request.user
            user_info = {
                'user_id': user.user_id,
                'email': user.email,
                'name': user.name,
                'picture_id': user.picture_id,
                'is_active': user.is_active,
                'is_admin': user.is_admin,
                'is_staff': user.is_staff,
            }
            return Response({'user_info': user_info})
        except MyUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
