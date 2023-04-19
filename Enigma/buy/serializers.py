from rest_framework import serializers
from buy.models import buyer, consumer, buy


from rest_framework import serializers
from .models import Group, buy, buyer, consumer

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class BuySerializer(serializers.ModelSerializer):
    groupID = GroupSerializer()
    
    class Meta:
        model = buy
        fields = '__all__'

class BuyerSerializer(serializers.ModelSerializer):
    buy = BuySerializer()
    
    class Meta:
        model = buyer
        fields = '__all__'

class ConsumerSerializer(serializers.ModelSerializer):
    buy = BuySerializer()
    
    class Meta:
        model = consumer
        fields = '__all__'
