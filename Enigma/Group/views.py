from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Group.models import Group, members
from Group.serializers import GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MemberSerializer

class ShowMembers(APIView):
 def post(self, request):
        try:
            group_id = request.data.get('groupID')
            group = Group.objects.get(id=group_id)
            member = members.objects.filter(groupID=group)
            serializer = MemberSerializer(member, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({'message': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class GroupInfo(APIView):

    def post(self, request):
        inf = Group.objects.filter(id=request.data['id']).values()
        info = GroupSerializer(instance=inf, many=True)
        return Response(info.data)


class DeleteGroup(APIView):

    def post(self, request):
        dele = Group.objects.filter(id=request.data['id']).delete()
        return Response(status=status.HTTP_200_OK)


