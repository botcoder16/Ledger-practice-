from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
   
class Group(models.Model):
    groupId=models.AutoField(primary_key=True)
    groupName=models.TextField(max_length=30)
    users=models.ManyToManyField(User)
    no_of_users=models.IntegerField(default=2)
    time=models.DateTimeField(default=now)
    
    def __str__(self):
        return str(self.groupId) + ' -> '+ self.groupName

class Transaction(models.Model):
    sender_name=models.CharField(max_length=30)
    reciever_name=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.IntegerField()
    groupId=models.ForeignKey(Group,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender_name + " -> " + str(self.reciever_name)