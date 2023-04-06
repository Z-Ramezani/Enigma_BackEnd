from operator import mod
from statistics import mode
from django.db import models
from Group.models import Group

from MyUser.models import MyUser


class buy(models.Model):

    groupID = models.ForeignKey(
        Group, related_name='groupID', on_delete=models.CASCADE)
    description: models.TextField(max_length=100)
    cost = models.BigIntegerField()
    date = models.DateField()
    picture_id = models.IntegerField(blank=False, default=0)


class buyer(models.Model):
    buy = models.ForeignKey(buy, related_name='Buyers',
                            on_delete=models.CASCADE)
    userID = models.ForeignKey(
        MyUser, related_name='userID_buy', on_delete=models.CASCADE)
    added_by = models.IntegerField(null=False)


class consumer(models.Model):
    consum = models.ForeignKey(
        buy, related_name='consumers', on_delete=models.CASCADE)
    userID = models.ForeignKey(
        MyUser, related_name='userID_cons', on_delete=models.CASCADE)


class consum_contrib(models.Model):
    consumeID = models.ForeignKey(consumer, on_delete=models.CASCADE)
    percent = models.FloatField()


class buyer_contrib(models.Model):
    buyerID = models.ForeignKey(buyer, on_delete=models.CASCADE)
    percent = models.FloatField()
