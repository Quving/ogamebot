from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account(models.Model):
    owner = models.ForeignKey(User, related_name='accounts', on_delete=models.CASCADE)
    username = models.CharField(default="", max_length=24)
    password = models.CharField(default="", max_length=24)
