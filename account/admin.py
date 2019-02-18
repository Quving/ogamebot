# Register your models here.
from django.contrib.admin import site

from account.models import Account

site.register(Account)
