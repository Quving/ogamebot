# Create your models here.

from django.db import models
from django.utils import timezone

from planet.models import Planet


class Mine(models.Model):
    planet = models.ForeignKey(Planet, related_name='mines', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    uptimed_at = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=0)
    upgradeable = models.BooleanField(default=False)
    name = models.CharField(default="", max_length=24)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


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
