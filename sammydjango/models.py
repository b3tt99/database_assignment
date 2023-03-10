import datetime

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    plate = models.CharField(max_length=8, default='00')
    gender = models.CharField(max_length=50, blank=False, null=False)
    LID = models.CharField(max_length=8, blank=False, default='00000000')
    DOI = models.CharField(max_length=20, default=datetime.date.today())
    ED = models.CharField(max_length=20,default=datetime.date.today())

def __str__(self):
    return self.name