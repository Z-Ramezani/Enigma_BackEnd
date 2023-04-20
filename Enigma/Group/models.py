from django.db import models

from MyUser.models import MyUser


class Group(models.Model):

    name = models.CharField(max_length=100, null=True)
    currency = models.CharField(max_length=100, default="تومان")


class Members(models.Model):
    groupID = models.ForeignKey(
        Group, related_name='group', on_delete=models.CASCADE)

    userID = models.ForeignKey(
        MyUser, related_name='member', on_delete=models.CASCADE, null=True)
