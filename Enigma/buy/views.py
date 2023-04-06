from datetime import date
from tokenize import group
from urllib import response
from rest_framework.views import APIView

from buy.models import buy
from buy.serializers import buySerializer 

class Buys(APIView):

    def all_group_buys(self, request):
        perch = buy.objects.filter( groupID=request.data['groupID'] ).values()
        perchase = buySerializer(instance=perch, many=True)
        return response(perchase)

    def user_group_buys(self, request):
        perch = buy.objects.filter( groupID=request.data['groupID'] , userID=request.data['userID'] ).values()
        perchase = buySerializer(instance=perch, many=True)
        return response(perchase)

