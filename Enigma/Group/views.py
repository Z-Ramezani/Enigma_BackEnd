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
        return Response(serializer_data.errors)

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
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            members = Members.objects.filter(groupID=request.data['groupID'])
            data = {}
            show_member = {}
            show_members = []

            for member in members:
                data['userID'] = member.userID.user_id
                data['groupID'] = request.data['groupID']
                cost = AmountofDebtandCredit.post(self=self, data=data)
                show_member['nema'] = member.userID.name
                show_member['cost'] = cost.data
                show_members.append(show_member)

            return Response(show_members, status=status.HTTP_200_OK)
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

    
class AmountofDebtandCredit(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, data):
        if not isinstance(data, dict):
            data = data.data
        serializer_data = AmountDebtandCreditMemberSerializer(data=data)
        print(serializer_data)
        if serializer_data.is_valid():
            list_buyer = buyer.objects.filter(userID = data['userID'])
            list_consumer = consumer.objects.filter(userID = data['userID'])

            sum = 0
            for buy in list_buyer:
                sum += buy.percent
            
            for buy in list_consumer:
                sum -= buy.percent

            return Response(sum)
        return Response(serializer_data.errors)
    

class DeleteGroup(APIView):

    def post(self, request):
        try:
            dele = Group.objects.filter(id=request.data['groupID']).delete()
            return Response({'message': 'Group deleted successfully.'}, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({'message': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# def DebtandCredit(member_id):
#             list_buyer = buyer.objects.filter(userID = member_id)
#             list_consumer = consumer.objects.filter(userID = member_id)
#             sum = 0
#             for buy in list_buyer:
#                 sum += buy.percent            
#             for buy in list_consumer:
#                 sum -= buy.percent
#             return  (sum)





# {
#   "name":"گروه دوستان",
#   "description":"دوستان دانشگاهی",
#   "currency":"تومان"
# }


# {
#   "emails":["maryam.shafizadegan.8098@gmail.com", "flowerfatmi5@gmail.com"]
# }
