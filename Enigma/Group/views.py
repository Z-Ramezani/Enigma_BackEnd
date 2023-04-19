from django.shortcuts import render
from .models import Group, Members
from .serializers import GroupSerializer, MembersSerializer, AmountDebtandCreditMemberSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from MyUser.models import MyUser
from buy.models import buyer, consumer

class CreateGroup(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        serializer_data = GroupSerializer(data=request.data)
        print(serializer_data)
        print(type(serializer_data))
        print("------------------------------------------------------------------")
        if serializer_data.is_valid():
            new_group = serializer_data.save()
            print(new_group)
            print(type(new_group))
            print("------------------------------------------------------------------")
            group_id = new_group.id
            return Response(group_id)
        return Response(serializer_data.errors)

class AddUserGroup(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self, request):
        serializer_data = MembersSerializer(data=request.data)

        if serializer_data.is_valid():
            print(request.data['emails'])
            print("------------------------------------------------------------------")
            for emailUser in request.data['emails']:
                user = MyUser.objects.get(email=emailUser)
                print(user)
                print(type(user))
                print("------------------------------------------------------------------")
                group = Group.objects.get(id=request.data['groupID'])
                member = Members(groupID=group, userID=user)
                print(member)
                print("------------------------------------------------------------------")
                member.save()
            return Response(status=status.HTTP_200_OK)
        #massage = {"massage":"ایمیل درست نیست"}
        #return Response(status=status.HTTP_400_BAD_REQUEST, data=massage)
        return Response(serializer_data.errors)


class DeleteGroup(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer

    def post(self, request):
        Group.objects.filter(groupID=request.data['id']).delete()
        return Response(status=status.HTTP_200_OK)
    
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