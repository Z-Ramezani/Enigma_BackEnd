from rest_framework import serializers
from Group.models import Group, members
from buy.serializers import buySerializer


class membersSerializer(serializers.ModelSerializer):
    userID = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    groupID = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = members
        fields = "__all__"

class showMembersSerializer(serializers.ModelSerializer):
    # userID = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # groupID = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = members
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    #members = membersSerializer(many=True)
    #buys = buySerializer(many=True)

    class Meta:
        model = Group
        fields = "__all__"
