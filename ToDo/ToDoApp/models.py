from django.db import models
import datetime

# Create your models here.
class SignUpDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)

class Projects(models.Model):
    Title = models.CharField(max_length=100,null=True,blank=True)
    Cdate =  models.DateField(default=datetime.date.today)

class TaskDB(models.Model):
    TitleT = models.CharField(max_length=100, null=True, blank=True)
    Task = models.CharField(max_length=100,null=True,blank=True)
    Discription = models.CharField(max_length=100,null=True,blank=True)
    status = models.BooleanField(default=False)
    Cdate =  models.DateField(default=datetime.date.today)
    Udate =  models.DateField(default=datetime.date.today)

