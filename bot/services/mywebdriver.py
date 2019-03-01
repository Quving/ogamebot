import os
import platform

from selenium import webdriver


class MyWebdriver:
    def __init__(self, remote=True, browser="chrome"):
        if not remote and platform.system() == "Darwin":
            options = webdriver.ChromeOptions()
            options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
            options.add_argument("--kiosk");
            self.driver = webdriver.Chrome(chrome_options=options)
        elif remote and browser == "firefox":
            selenium_hub_host = os.getenv("SELENIUM_HUB_HOST")
            selenium_hub_url = "http://" + selenium_hub_host + "/wd/hub"
            self.driver = webdriver.Remote(command_executor=selenium_hub_url,
                                           desired_capabilities={'browserName': 'firefox'})
            # self.driver.set_window_size(1500, 1080)
        else:  # remote and browser == "chrome":
            selenium_hub_host = os.getenv("SELENIUM_HUB_HOST")
            selenium_hub_url = "http://" + selenium_hub_host + "/wd/hub"
            options = webdriver.ChromeOptions()
            options.add_argument("--kiosk");
            self.driver = webdriver.Remote(command_executor=selenium_hub_url,
                                           desired_capabilities=options.to_capabilities())
            # self.driver.set_window_size(1500, 1080)
        self.driver.implicitly_wait(10)
