# Create your models here.

from django.db import models

from planet.models import Planet


class Mine(models.Model):
    planet = models.ForeignKey(Planet, related_name='mines', on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    upgradeable = models.BooleanField(default=False)
    name = models.CharField(default="", max_length=24)

    def __str__(self):
        return self.name


class MetalMine(Mine):
    Mine.name = "MetalMine"


class CrystalMine(Mine):
    Mine.name = "CrystalMine"


class DeuteriumMine(Mine):
    Mine.name = "DeuteriumMine"


class SolarPowerstation(Mine):
    Mine.name = "SolarPowerstation"


class FusionReactor(Mine):
    Mine.name = "FusionReactor"


class SolarSatellite(Mine):
    Mine.name = "SolarSatellite"
