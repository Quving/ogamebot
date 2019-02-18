from django.db import models

# Create your models here.
from planet.models import Planet


class Inventory(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    iron = models.IntegerField(default=0)
    crystal = models.IntegerField(default=0)
    deuterium = models.IntegerField(default=0)
    energy = models.IntegerField(default=0)

    def energy_is_positiv(self):
        return self.energy > 0
