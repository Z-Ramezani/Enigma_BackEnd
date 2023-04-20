from rest_framework.response import Response
from rest_framework.views import APIView
from Group.models import Group, Members
from Group.serializers import GroupSerializer
from rest_framework import status
from .serializers import MemberSerializer


class ShowMembers(APIView):
    def post(self, request):
        try:
            group_id = request.data.get('groupID')
            group = Group.objects.get(id=group_id)
            member = Members.objects.filter(groupID=group)
            serializer = MemberSerializer(member, many=True)
                                      # Update each member's cost
            #for member in serializer.data:
                #member_id = member['id']
                                       # Call dobet function to get cost for this member
                #cost = dobet(member_id)
                #member['cost'] = cost

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({'message': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GroupInfo(APIView):
    def post(self, request):
        try:
            group_id = request.data.get('groupID')
            group = Group.objects.get(id=group_id)
            serializer = GroupSerializer(group)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({'message': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteGroup(APIView):

    def post(self, request):
        try:
            dele = Group.objects.filter(id=request.data['groupID']).delete()
            return Response({'message': 'Group deleted successfully.'}, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({'message': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
