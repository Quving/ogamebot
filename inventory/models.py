from django.db import models

# Create your models here.
from planet.models import Planet


class Inventory(models.Model):
    planet = models.ForeignKey(Planet, related_name='inventory', on_delete=models.CASCADE)
    metal = models.IntegerField(default=0)
    crystal = models.IntegerField(default=0)
    deuterium = models.IntegerField(default=0)
    dark_matter = models.IntegerField(default=0)
    energy = models.IntegerField(default=0)
