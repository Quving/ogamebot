# Register your models here.
from django.contrib.admin import site

from mine.models import MetalMine, DeuteriumMine, CrystalMine, SolarSatellite, FusionReactor, SolarPowerstation

site.register(FusionReactor)
site.register(MetalMine)
site.register(DeuteriumMine)
site.register(CrystalMine)
site.register(SolarPowerstation)
site.register(SolarSatellite)
