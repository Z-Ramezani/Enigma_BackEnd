from urllib import response
from rest_framework.views import APIView

from Group.models import Group
from Group.serializers import GroupSerializer


class GroupView(APIView):

    def GroupInfo(self, request):
        inf = Group.objects.filter(groupID=request.data['groupID']).values()
        info = GroupSerializer(instance=inf, many=True)
        return response(info)

    def Delete_Group(self, request):
        dele = Group.objects.filter(groupID=request.data['groupID']).delete()
        return response("done")
