import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Interactor:
    def __init__(self, account, driver, logger):
        self.driver = driver
        self.account = account
        self.logger = logger
        self.username = account.username
        self.password = account.password
        self.is_logged_in = False
        self.login_url = "https://lobby.ogame.gameforge.com/de_DE/?language=de"
        self.base_login_url = 'https://s158-de.ogame.gameforge.com'
        self.report = {}

        if logger is None:
            self.logger = logging.getLogger('ogamebot')
            self.logger.setLevel(logging.DEBUG)
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            ch.setLevel(logging.DEBUG)
            self.logger.addHandler(ch)

    def goto(self, view_id="", planet_id=""):
        if not self.is_logged_in:
            self.login()

        self.driver.get('{}/game/index.php?page={}&cp={}'.format(
            self.base_login_url,
            view_id,
            planet_id
        ))

    def login(self):
        self.logger.info("Log {} in.".format(self.account.playername))
        self.driver.get(self.login_url)
        assert "OGame" in self.driver.title
        self.driver.find_elements_by_css_selector("#loginRegisterTabs .tabsList span")[0].click()
        self.driver.find_elements_by_css_selector("#loginForm input")[0].send_keys(self.username)
        self.driver.find_elements_by_css_selector("#loginForm input")[1].send_keys(self.password)
        self.driver.find_element_by_css_selector('#loginForm button').click()
        WebDriverWait(self.driver, 15).until(EC.title_is("OGame Lobby"))
        self.driver.find_element_by_css_selector("button.button.button-default").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 15).until(EC.title_is("Fenrir OGame"))
        self.logger.info("Login succeeded.".format(self.account.playername))
        self.is_logged_in = True
