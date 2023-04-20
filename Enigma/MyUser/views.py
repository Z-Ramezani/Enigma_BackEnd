from django.shortcuts import render
from .models import MyUser
from .serializers import MyUserSerializer, UpdateUserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .serializers import MyUserSerializer, ChangePasswordSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyUser

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



class UserInfo(APIView):
    def post(self, request):
        try:
            user_id = request.data.get('userID')
            user = MyUser.objects.get(user_id=user_id)
            user_info = {
                'user_id': user.user_id,
                'email': user.email,
                'username': user.username,
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
