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
            buys = buy.objects.filter(groupID=group_id, Buyers__userID=user_id)
            serializer = BuySerializer(buys, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            

    """
    def user_group_buys(self, request):
        perch = buy.objects.filter( groupID=request.data['groupID'] , userID=request.data['userID'] ).values()
        perchase = buySerializer(instance=perch, many=True)
        return response(perchase)
    """
