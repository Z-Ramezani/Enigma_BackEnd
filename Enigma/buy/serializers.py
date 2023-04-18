from rest_framework import serializers
from buy.models import buyer, consumer, buy


class buyerSerializer(serializers.ModelSerializer):


    class Meta:
        model = buyer
        fields = "__all__"


class consumerSerializer(serializers.ModelSerializer):

    class Meta:
        model = consumer
        fields = "__all__"


class buySerializer(serializers.ModelSerializer):
    buyers = buyerSerializer(many=True, read_only=True)
    consumers = consumerSerializer(many=True, read_only=True)

    class Meta:
        model = buy
        fields = "__all__"