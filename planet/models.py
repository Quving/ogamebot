from django.db import models

# Create your models here.
from account.models import Account


class Planet(models.Model):
    account = models.ForeignKey(Account, default=0, on_delete=models.CASCADE)
    id = models.CharField(max_length=50, default="", unique=True, primary_key=True)
    name = models.CharField(default="", max_length=16)
