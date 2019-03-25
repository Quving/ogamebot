from __future__ import absolute_import, unicode_literals

from celery import task
from celery.utils.log import get_task_logger

from account.models import Account
from bot.services.crawler import Crawler
from bot.services.mywebdriver import MyWebdriver
from bot.services.stacker import Stacker

logger = get_task_logger(__name__)


@task()
def crawl():
    logger.info("Update accounts...")
    for account in Account.objects.all():
        if account.bot.crawler_enabled:
            # Create driver
            mywebdriver = MyWebdriver(remote=True, browser="chrome").driver

            # Crawl Account
            crawler = Crawler(account, driver=mywebdriver, logger=logger)
            crawler.crawl()

            # Close driver
            mywebdriver.quit()


@task()
def stack():
    for account in Account.objects.all():
        if account.bot.stacker_enabled:
            # Create driver
            mywebdriver = MyWebdriver(remote=True, browser="chrome").driver

            # Crawl Account
            stacker = Stacker(account, driver=mywebdriver, logger=logger)
            stacker.stack()

            # Close driver
            mywebdriver.quit()
