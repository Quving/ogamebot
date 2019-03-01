from django.db import models

# Create your models here.
from account.models import Account


class Coordinate(models.Model):
    x = models.CharField(default="", max_length=3)
    y = models.CharField(default="", max_length=3)
    z = models.CharField(default="", max_length=3)

    def __str__(self):
        return "{}:{}:{}".format(self.x, self.y, self.z)


class Planet(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    account = models.ForeignKey(Account, related_name='planets', on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=32)
    coord = models.ForeignKey(Coordinate, related_name='planet', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name
