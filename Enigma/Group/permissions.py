from rest_framework.permissions import BasePermission
from MyUser.models import MyUser
from myapp.models import Group, Members



class IsGroupUser(BasePermission):
    def has_permission(self, request, view):

        is_group_member = False
        user = request.user
        group = Group.objects.get(request.data.groupID)
        members = Members.objects.filter(userID=user, groupID=group)
        if members:
            is_group_member = True   
        return request.user and request.user.is_authenticated and is_group_member



