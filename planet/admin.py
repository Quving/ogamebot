# Register your models here.
from django.contrib.admin import site

from planet.models import Planet

site.register(Planet)
