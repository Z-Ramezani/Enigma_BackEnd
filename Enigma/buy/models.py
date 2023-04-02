from operator import mod
from django.db import models
from Group.models import Group

from MyUser.models import MyUser


class buy(models.Model):

    groupID = models.ForeignKey(
        Group, related_name='groupID', on_delete=models.CASCADE)
    cost = models.BigIntegerField()
    date = models.DateField()
    picture_id = models.IntegerField(blank=False, default=0)


class buyer(models.Model):
    buy = models.ForeignKey(buy, related_name='Buyers',
                            on_delete=models.CASCADE)
    userID = models.ForeignKey(
        MyUser, related_name='userID', on_delete=models.CASCADE)
    percent = models.IntegerField()


class consumer(models.Model):
    consum = models.ForeignKey(
        buy, related_name='consumers', on_delete=models.CASCADE)
    userID = models.ForeignKey(
        MyUser, related_name='userID', on_delete=models.CASCADE)
    percent = models.IntegerField()
