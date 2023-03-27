from django.db import models

class buy(models.Model):

    buyID = models.IntegerField()
    groupID = models.ForeignKey(group, related_name='groupID', on_delete=models.CASCADE)
    cost = models.BigIntegerField()
    
class buyer(models.Model):
    buy = models.ForeignKey(buy, related_name='Buyers', on_delete=models.CASCADE)
    userID = models.ForeignKey(user, related_name='userID', on_delete=models.CASCADE)
    percent = models.IntegerField()
    
class consumer(models.Model):
    consum = models.ForeignKey(buy, related_name='consumers', on_delete=models.CASCADE)
    userID = models.ForeignKey(user, related_name='userID', on_delete=models.CASCADE)
