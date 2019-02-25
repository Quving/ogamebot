import json

from account.models import Account
from bot.services.crawler import Crawler
from bot.services.mywebdriver import MyWebdriver


def toJson(data):
    with open("becks.json", "w") as file:
        file.write(json.dumps(data, ensure_ascii=False, indent=4))


def run():
    for account in Account.objects.all():
        # Create driver
        mywebdriver = MyWebdriver(remote=False).driver

        # Crawl Account
        crawler = Crawler(account, driver=mywebdriver)
        crawler.crawl()
        toJson(crawler.report)

        # Close driver
        mywebdriver.quit()
