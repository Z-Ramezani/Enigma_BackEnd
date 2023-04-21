from rest_framework import serializers
from rest_framework import serializers
from Group.models import Group
from MyUser.models import MyUser
from .models import buy, buyer, consumer


class buyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = buyer
        fields = "__all__"
    
    def create(self, validated_data):
        new_buyer = buyer.objects.create(**validated_data)
        print(new_buyer)
        print("-------------------------------------------------")
        return new_buyer


class consumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumer
        fields = "__all__"
    
    def create(self, validated_data):
        new_consumer = consumer.objects.create(**validated_data)
        print(new_consumer)
        print("-------------------------------------------------")
        return new_consumer


class buySerializer(serializers.ModelSerializer):
    class Meta:
        model = buy
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'picture_id']


class BuyerSerializer(serializers.ModelSerializer): 
    userID = MyUserSerializer()

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = buyer
        fields = ['userID', 'percent']

class ConsumerSerializer(serializers.ModelSerializer):
    userID = MyUserSerializer()

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumer
        fields = ['userID', 'percent']


class BuySerializer(serializers.ModelSerializer):
    Buyers = BuyerSerializer(many=True, read_only=True)
    consumers = ConsumerSerializer(many=True, read_only=True)

    class Meta:
        model = buyer
        fields = ['userID', 'percent']
