from locale import currency
from django.db import models

from MyUser.models import MyUser


class Group(models.Model):

<<<<<<< Updated upstream
    name = models.CharField(max_length=100, null=True)
=======
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True, null=True)
>>>>>>> Stashed changes
    currency = models.CharField(max_length=100, default="تومان")


class members(models.Model):
    groupID = models.ForeignKey(
        Group, related_name='group', on_delete=models.CASCADE)
    
    userID = models.ForeignKey(
        MyUser, related_name='member', on_delete=models.CASCADE)