
from rest_framework import serializers
from .models import MyUser, Group, Members

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'picture_id')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    groupID = GroupSerializer(read_only=True)
    userID = MyUserSerializer(read_only=True)

    class Meta:
        model = Members
        fields = '__all__'
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

