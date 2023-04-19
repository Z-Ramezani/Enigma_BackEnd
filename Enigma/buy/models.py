from django.db import models
from Group.models import Group
from MyUser.models import MyUser


class buy(models.Model):

    groupID = models.ForeignKey(
        Group, related_name='groupID', on_delete=models.CASCADE)

    
    description: models.TextField(max_length=100)
    cost = models.BigIntegerField()
    date = models.IntegerField()
    picture_id = models.IntegerField(blank=False, default=0)
    added_by = models.IntegerField(null=False)


class buyer(models.Model):
    buy = models.ForeignKey(buy, related_name='Buyers',
                            on_delete=models.CASCADE)
    userID = models.ForeignKey(
        MyUser, related_name='userID_buy', on_delete=models.CASCADE)
    percent = models.FloatField()


class consumer(models.Model):
    buy = models.ForeignKey(
        buy, related_name='consumers', on_delete=models.CASCADE)
    userID = models.ForeignKey(
        MyUser, related_name='userID_cons', on_delete=models.CASCADE)
    percent = models.FloatField()
