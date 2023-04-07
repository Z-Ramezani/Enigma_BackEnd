from urllib import response
from rest_framework.views import APIView

from Group.models import buy
from buy.serializers import buySerializer 

class Group(APIView):

    def GroupInfo(self, request):
        perch = buy.objects.filter( groupID=request.data['groupID'] ).values()
        perchase = buySerializer(instance=perch, many=True)
        return response(perchase)

    def Delete_Group(self, request):
        perch = buy.objects.filter( groupID=request.data['groupID'] ).
        perchase = buySerializer(instance=perch, many=True)
        return response(perchase)

