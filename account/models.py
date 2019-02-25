from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    playername = models.CharField(default="", max_length=24, blank=True)
    username = models.CharField(default="", max_length=24)
    password = models.CharField(default="", max_length=24)

    def __str__(self):
        return self.playername
