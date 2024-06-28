from email.header import Header
from django.db import models





class TaskModel(models.Model):
    header= models.CharField(max_length=75) 
    desc= models.TextField()
    data= models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=False)
# Create your models here.
