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

class AmountDebtandCreditMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"