from rest_framework import serializers
from Group.models import Group, members


class membersSerializer(serializers.ModelSerializer):
    member = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = members
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    members = membersSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = "__all__"
