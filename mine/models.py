from django.db import models

# Create your models here.
from planet.models import Planet


class Mine(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=0)
    upgradeable = models.BooleanField(default=False)
    name = models.CharField(default="",
                            max_length=15)


class IronMine(Mine):
    Mine.name = "Iron_Mine"


class CrystalMine(Mine):
    Mine.name = "Crystal_Mine"


class DeuteriumMine(Mine):
    Mine.name = "Deuterium_Mine"
