# from rest_framework import serializers
# from buy.models import buyer, consumer, buy


# class buyerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = buyer
#         fields = "__all__"


# class consumerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = consumer
#         fields = "__all__"


# class buySerializer(serializers.ModelSerializer):
#     buyers = buyerSerializer(many=True, read_only=True)
#     consumers = consumerSerializer(many=True, read_only=True)

#     class Meta:
#         model = buy
#         fields = "__all__"


from rest_framework import serializers
from Group.models import Group
from MyUser.models import MyUser
from .models import buy, buyer, consumer


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
