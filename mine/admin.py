from django.contrib import admin

# Register your models here.
from django.contrib.admin import site

from mine.models import Mine

site.register(Mine)
