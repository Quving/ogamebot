from __future__ import absolute_import, unicode_literals

from celery import task
from celery.utils.log import get_task_logger

from account.models import Account
from bot.services.mywebdriver import MyWebdriver
from bot.services.stacker import Stacker

logger = get_task_logger(__name__)


@task()
def crawl():
    logger.info("Update accounts...")


@task()
def stack():
    for account in Account.objects.all():
        # Create driver
        mywebdriver = MyWebdriver(remote=True, browser="chrome").driver

        # Crawl Account
        stacker = Stacker(account, driver=mywebdriver, task_logger=logger)
        stacker.stack()

        # Close driver
        mywebdriver.quit()
