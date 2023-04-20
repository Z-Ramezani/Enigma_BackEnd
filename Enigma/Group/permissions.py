from rest_framework.permissions import BasePermission
from MyUser.models import MyUser
from .models import Group, Members



class IsGroupUser(BasePermission):
    def has_permission(self, request, view):
        print("--------------------------------------------------------------------------------")
        is_group_member = False
        members = Members.objects.filter(userID=request.user, groupID=request.data['groupID'])
        if members:
            is_group_member = True 
        return request.user and request.user.is_authenticated and is_group_member



