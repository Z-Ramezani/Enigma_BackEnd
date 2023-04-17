from rest_framework import status
from rest_framework.response import Response
from urllib import response
from rest_framework.views import APIView
from Group.models import Group, members
from Group.serializers import GroupSerializer, showMembersSerializer


class GroupInfo(APIView):

    def post(self, request):
        inf = Group.objects.filter(id=request.data['id']).values()
        info = GroupSerializer(instance=inf, many=True)
        return Response(info.data)


class DeleteGroup(APIView):

    def post(self, request):
        dele = Group.objects.filter(groupID=request.data['id']).delete()
        return response(status=status.HTTP_200_OK)


class ShowMembers(APIView):
    def post(self, request):
        serializer_data = showMembersSerializer(data=request.data)

        if serializer_data.is_valid():
            gro = members.objects.filter(groupID=request.data['groupID'])
            listmember = []
            for member in gro:
                listmember.append(
                    [member.userID.username, member.userID.picture_id])
            return Response(listmember)
        return Response(serializer_data.errors)
