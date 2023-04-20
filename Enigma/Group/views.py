from rest_framework.response import Response
from Group.models import Group, Members
from buy.models import buyer, consumer
from .serializers import MemberSerializer
from django.shortcuts import render
from .serializers import GroupSerializer, MemberSerializer, AmountDebtandCreditMemberSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from MyUser.models import MyUser
from .permissions import IsGroupUser

class ShowGroups(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            user_groups = Members.objects.filter(userID=self.request.user.user_id)
            return Response(user_groups.values())
        except Members.DoesNotExist:
            return Response({'error': 'User does not belong to any groups'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

class CreateGroup(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer_data = GroupSerializer(data=request.data)
        if serializer_data.is_valid():
            new_group = serializer_data.save()
            group_id = new_group.id
            data = {}
            data["groupID"] = group_id
            data["emails"] = request.data['emails']
            data["emails"].append(str(self.request.user.email))
            print(data)
            AddUserGroup.post(self = self, data=data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors)

class AddUserGroup(APIView):
    permission_classes = [permissions.IsAuthenticated and IsGroupUser]
    def post(self, data):
        if not isinstance(data, dict):
            data = data.data
        serializer_data = MemberSerializer(data=data)
        if serializer_data.is_valid():
            for emailUser in data['emails']:
                try:
                    user = MyUser.objects.get(email=emailUser)
                    group = Group.objects.get(id=data['groupID'])
                    member = Members(groupID=group, userID=user)
                    member.save()
                except MyUser.DoesNotExist:
                    return Response({'message': 'user not found.'}, status=status.HTTP_404_NOT_FOUND)
                
            return Response(status=status.HTTP_200_OK)
        #massage = {"massage":"ایمیل درست نیست"}
        #return Response(status=status.HTTP_400_BAD_REQUEST, data=massage)
        return Response(serializer_data.errors)


    
class AmountofDebtandCredit(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        serializer_data = AmountDebtandCreditMemberSerializer(data=request.data)
        if serializer_data.is_valid():
            list_buyer = buyer.objects.filter(userID = request.data['userID'])
            list_consumer = consumer.objects.filter(userID = request.data['userID'])

            print(list_buyer)
            print("_______________________________________________________")
            print(list_consumer)
            print("_______________________________________________________")

            sum = 0
            for buy in list_buyer:
                sum += buy.percent
            
            for buy in list_consumer:
                sum -= buy.percent

            return Response(sum)
        return Response(serializer_data.errors)






# {
#   "name":"گروه دوستان",
#   "description":"دوستان دانشگاهی",
#   "currency":"تومان"
# }


# {
#   "emails":["maryam.shafizadegan.8098@gmail.com", "flowerfatmi5@gmail.com"]
# }
