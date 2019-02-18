from django.db import models

# Create your models here.
from account.models import Account


class Bot(models.Model):
    bot_enabled = models.BooleanField(default=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    copy_mines_with_main_planet = models.BooleanField(default=False)