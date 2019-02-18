from django.db import models

# Create your models here.
from planet.models import Planet


class Fleet(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
