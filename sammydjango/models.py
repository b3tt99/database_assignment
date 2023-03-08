from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(default='Kenya', max_length=50)
    city = models.CharField(default='Nairobi', max_length=50)

def __str__(self):
    return self.name