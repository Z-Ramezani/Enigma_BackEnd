from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from .models import buy
from .serializers import BuySerializer, buySerializer, buyerSerializer, consumerSerializer
from MyUser.models import MyUser


class CreateBuy(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer_data_buy = buySerializer(data=request.data)

        if serializer_data_buy.is_valid():
            new_buy = serializer_data_buy.save()
            buy_id = new_buy.id
            data = {}
            data['buy'] = new_buy

            list_buyer = request.data['buyer']
            list_consumer = request.data['consumer']

            for buyer in list_buyer:
                user = MyUser.objects.get(name=buyer['name'], picture_id=buyer['picture_id'])
                data['userID'] = user
                data['percent'] = buyer['cost']
                print(data)
                print("-----------------------------------------------------")
                serializer_data_buyer = buyerSerializer(data=data)

                print(serializer_data_buyer.is_valid())
                if serializer_data_buyer.is_valid():
                    serializer_data_buyer.save()

            for consumer in list_consumer:
                user = MyUser.objects.get(name=consumer['name'], picture_id=consumer['picture_id'])
                data['userID_cons'] = user
                data['percent'] = consumer['cost']
                print(data)
                print("-----------------------------------------------------")
                serializer_data_consumer = consumerSerializer(data=data)

                print(serializer_data_consumer.is_valid())
                if serializer_data_consumer.is_valid():
                    serializer_data_consumer.save()
            
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer_data_buy.errors)


class GetGroupBuys(APIView):

    def post(self, request):
        perch = buy.objects.filter(
            groupID=request.data['groupID'])
        perchase = BuySerializer(perch, many=True)
        return Response(perchase.data)

class UserGroupBuys(APIView):
    def post(self, request):
        try:
            user_id = request.data.get('userID')
            group_id = request.data.get('groupID')

            # Get buys where the user is a buyer
            buyer_buys = buy.objects.filter(
                Buyer__userID=user_id, groupID=group_id).distinct()
            buyer_serializer = BuySerializer(buyer_buys, many=True)

            # Get buys where the user is a consumer
            consumer_buys = buy.objects.filter(
                consumer__userID=user_id, groupID=group_id).distinct()
            consumer_serializer = BuySerializer(consumer_buys, many=True)

            response_data = {
                'buyer_buys': buyer_serializer.data,
                'consumer_buys': consumer_serializer.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
