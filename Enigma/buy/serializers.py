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
from .models import buy, buyer, consumer

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = buyer
        fields = ('id', 'buy', 'userID', 'percent')

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumer
        fields = ('id', 'consum', 'userID', 'percent')

class BuySerializer(serializers.ModelSerializer):
    Buyers = BuyerSerializer(many=True, read_only=True)
    Consumers = ConsumerSerializer(many=True, read_only=True)
    class Meta:
        model = buy
        fields = ('id', 'groupID', 'cost', 'date', 'picture_id', 'added_by', 'Buyers', 'Consumers')