from rest_framework.response import Response
from rest_framework.views import APIView

from buy.models import buy
from buy.serializers import buySerializer


class GetGroupBuys(APIView):

    def post(self, request):
        perch = buy.objects.filter(
            groupID=request.data['groupID']).values()
        perchase = buySerializer(instance=perch, many=True)
        return Response(perchase.data)
    """
    def user_group_buys(self, request):
        perch = buy.objects.filter( groupID=request.data['groupID'] , userID=request.data['userID'] ).values()
        perchase = buySerializer(instance=perch, many=True)
        return response(perchase)
    """
