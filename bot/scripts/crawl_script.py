from account.models import Account
from bot.services.crawler import Crawler
from bot.services.mywebdriver import MyWebdriver


def run():
    for account in Account.objects.all():
        # Create driver
        if account.bot.crawler_enabled:
            mywebdriver = MyWebdriver(remote=False, browser="chrome").driver

            # Crawl Account
            crawler = Crawler(account, driver=mywebdriver)
            crawler.crawl()

            # Close driver
            mywebdriver.quit()
