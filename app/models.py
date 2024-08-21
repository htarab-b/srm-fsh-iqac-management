from django.db import models
import datetime

# Choices
types = [
    ['Staff', 'Staff'],
    ['Student', 'Student']
]

# Create your models here.
class FormDetailsModel(models.Model):
    Type = models.CharField(max_length=15, choices=types)
    Name = models.CharField(max_length=35)
    RegID = models.CharField(max_length=25)
    Department = models.CharField(max_length=55)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=25)
    Subject = models.CharField(max_length=155)
    Purpose = models.CharField(max_length=255)
    Date = models.DateField(default=datetime.datetime.today)
    Coordinator_Approval = models.CharField(max_length=3, default="NO")
    Dean_Approval = models.CharField(max_length=3, default="NO")
    DeputyDean_Approval = models.CharField(max_length=3, default="NO")
    ProVC_Approval = models.CharField(max_length=3, default="NO")