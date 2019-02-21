from django.db import models

# Create your models here.
from planet.models import Planet


class Inventory(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    metal = models.FloatField(default=0)
    crystal = models.FloatField(default=0)
    deuterium = models.FloatField(default=0)
    dark_matter = models.FloatField(default=0)
    energy = models.FloatField(default=0)

    def energy_is_positiv(self):
        return self.energy > 0
