from locale import currency
from django.db import models

from MyUser.models import MyUser


class Group(models.Model):

    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    currency = models.CharField(max_length=100, default="تومان")


class members(models.Model):
    groupID = models.ForeignKey(
        Group, related_name='group', on_delete=models.CASCADE)
    memmberID = models.ForeignKey(
        MyUser, related_name="memmber", on_delete=models.CASCADE)