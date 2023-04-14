from .models import Group, Members
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

    def create(self, validated_data):
        new_group = Group.objects.create(**validated_data)
        return new_group


class MembersSerializer(serializers.Serializer):
    emails = serializers.ListField(child=serializers.EmailField())
    groupID = serializers.IntegerField()

    # userID = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='userID'
    # )
    # class Meta:
    #     model = Members
    #     fields = ["userID"]

class AmountDebtandCreditMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"

