import json

from account.models import Account
from bot.services.crawler import Crawler
from bot.services.mywebdriver import MyWebdriver
from bot.services.stacker import Stacker


def run():
    for account in Account.objects.all():
        # Create driver
        mywebdriver = MyWebdriver(remote=False).driver

        # Crawl Account
        stacker = Stacker(account, driver=mywebdriver)
        stacker.stack()

        # Close driver
        mywebdriver.quit()
