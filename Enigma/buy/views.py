from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from buy.models import buy
from buy.serializers import BuySerializer


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
