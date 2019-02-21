from __future__ import absolute_import, unicode_literals

from celery import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task()
def crawl():
    logger.info("Update accounts...")
    print("Miao")
    return "Watchiedoo"
