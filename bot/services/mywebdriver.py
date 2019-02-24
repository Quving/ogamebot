import os
import platform

from selenium import webdriver


class MyWebdriver:
    def __init__(self, remote=True):
        if not remote and platform.system() == "Darwin":
            options = webdriver.ChromeOptions()
            options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
            self.driver = webdriver.Chrome(chrome_options=options)
        else:
            selenium_hub_host = os.getenv("SELENIUM_HUB_HOST")
            selenium_hub_url = "http://" + selenium_hub_host + "/wd/hub"
            self.driver = webdriver.Remote(command_executor=selenium_hub_url,
                                           desired_capabilities={'browserName': 'firefox'})
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1800, 900)
