from .models import Group, Members
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

    def create(self, validated_data):
        new_group = Group.objects.create(**validated_data)
        return new_group


class MembersSerializer(serializers.ModelSerializer):
    userID = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    groupID = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Members
        fields = "__all__"

