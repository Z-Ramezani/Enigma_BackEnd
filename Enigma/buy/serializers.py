from rest_framework import serializers
from buy.models import buyer, consumer, buy

class buyerSerializer(serializers.ModelSerializer):
    categories = serializers.RelatedField(many=True, read_only=True)
    actions = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Filter
        fields = "__all__"


class buySerializer(serializers.ModelSerializer):
    buyers = buyerSerializer(many=True, read_only=True)

    class Meta:
        model = ServicesComponents
        fields = ('target_id','name','exported', 'permissionName','filterCheck', 'filters')