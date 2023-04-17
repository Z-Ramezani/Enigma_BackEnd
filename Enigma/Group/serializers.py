from rest_framework import serializers
from Group.models import Group, members


class showMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = members
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
