from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Account


class Bot(models.Model):
    crawler_enabled = models.BooleanField(default=False)
    builder_enabled = models.BooleanField(default=False)
    stacker_enabled = models.BooleanField(default=False)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.account.owner, self.account.username)


@receiver(post_save, sender=Account)
def create_account_bot(sender, instance, created, **kwargs):
    if created:
        Bot.objects.create(account=instance)


@receiver(post_save, sender=Account)
def save_user_carer(sender, instance, **kwargs):
    instance.bot.save()
