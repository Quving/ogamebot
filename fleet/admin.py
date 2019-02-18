# Register your models here.
from django.contrib.admin import site

from fleet.models import Fleet

site.register(Fleet)
