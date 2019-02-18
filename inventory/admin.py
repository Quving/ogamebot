# Register your models here.
from django.contrib.admin import site

from inventory.models import Inventory

site.register(Inventory)
