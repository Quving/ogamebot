from django.db import models

# Create your models here.
from account.models import Account


class Planet(models.Model):
    id = models.CharField(max_length=50, default="", unique=True, primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=16)
