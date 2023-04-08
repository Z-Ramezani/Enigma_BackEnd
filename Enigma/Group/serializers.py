from .models import Group, members
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", "description", "currency")
    
    class Meta:
        model = members
        fields = 