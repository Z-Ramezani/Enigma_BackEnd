from rest_framework.response import Response
from rest_framework.views import APIView
from Group.models import Group, Members
from buy.models import buyer, consumer
from Group.serializers import GroupSerializer
from rest_framework import status
from .serializers import MemberSerializer, AmountDebtandCreditMemberSerializer


class ShowMembers(APIView):
    def post(self, request):
        try:
            group_id = request.data.get('groupID')
            group = Group.objects.get(id=group_id)
            member = Members.objects.filter(groupID=group)
            serializer = MemberSerializer(member, many=True)
                                      # Update each member's cost
            for member in serializer.data:
                member_id = member['id']
                                       # Call dobet function to get cost for this member
                cost = DebtandCredit(member_id)

                member['cost'] = cost
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


def DebtandCredit(member_id):

            list_buyer = buyer.objects.filter(userID = member_id)
            list_consumer = consumer.objects.filter(userID = member_id)

            sum = 0
            for buy in list_buyer:
                sum += buy.percent
            
            for buy in list_consumer:
                sum -= buy.percent

            return  (sum)