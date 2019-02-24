from django.db import models

# Create your models here.
from planet.models import Planet


class Fleet(models.Model):
    planet = models.ForeignKey(Planet, related_name='fleet', on_delete=models.CASCADE)


class Ship(models.Model):
    name = models.CharField(default="", max_length=24)
    amount = models.IntegerField(default=0)


class SmallCargo(Ship):
    pass


class LargeCargo(Ship):
    pass


class ColonyShip(Ship):
    pass


class Recycler(Ship):
    pass


class LittleFiter(Ship):
    pass


class Deathstar(Ship):
    pass


class Destroyer(Ship):
    pass


class HeavyFiter(Ship):
    pass


class Cruiser(Ship):
    pass


class Battleship(Ship):
    pass


class Battlecruiser(Ship):
    pass


class Bomber(Ship):
    pass
