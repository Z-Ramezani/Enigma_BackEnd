from .models import MyUser

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotAcceptable
from rest_framework.exceptions import PermissionDenied

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "password", "user_id","username", "picture_id")
    

    user_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(max_length=50, required=True)
    picture_id = serializers.IntegerField(required=True)

   
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def validate_email(self, value):
        if get_user_model().objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("email exists.")
        return value