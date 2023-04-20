from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

from buy.models import buy
from buy.serializers import BuySerializer

class CreateBuy(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        serializer_data = BuySerializer(data=request.data)
        print(serializer_data)
        print(type(serializer_data))
        print("------------------------------------------------------------------")
        if serializer_data.is_valid():
            new_buy = serializer_data.save()
            print(new_buy)
            print(type(new_buy))
            print("------------------------------------------------------------------")
            buy_id = new_buy.id
            data = {}
            
            return Response(buy_id)
        return Response(serializer_data.errors)


class GetGroupBuys(APIView):

    def post(self, request):
        perch = buy.objects.filter(
        groupID=request.data['groupID']).values()
        perchase = BuySerializer(instance=perch, many=True)
        return Response(perchase.data)
    """
    def user_group_buys(self, request):
        perch = buy.objects.filter( groupID=request.data['groupID'] , userID=request.data['userID'] ).values()
        perchase = buySerializer(instance=perch, many=True)
        return response(perchase)
    """