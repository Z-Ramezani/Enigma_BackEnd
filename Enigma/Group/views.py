from django.shortcuts import render
from .models import Group, Members
from .serializers import GroupSerializer, MembersSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from MyUser.models import MyUser

class CreateGroup(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer

class AddUserGroup(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MembersSerializer

    def post(self, request):
        for user in MyUser.objects.all():
            #usr = MyUser.objects.filter(email=request.data['email']).values()
            if user.email == request.data['email']:
                user.save()

class DeleteGroup(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer

    def post(self, request):
        Group.objects.filter(groupID=request.data['id']).delete()
        return Response(status=status.HTTP_200_OK)


