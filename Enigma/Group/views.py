from rest_framework import status
from rest_framework.response import Response
from urllib import response
from rest_framework.views import APIView
from Group.models import Group, members
from Group.serializers import GroupSerializer, membersSerializer


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
        inf_member = members.objects.filter(
            groupID=request.data['groupID']).values()
        print(inf_member)
        info_member = membersSerializer(instance=inf_member, many=True)
        print("__________________________________________________________")
        print(info_member)
        print("__________________________________________________________")
        print(info_member.data)

        return Response(info_member.data)
