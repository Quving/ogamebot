from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Interactor:
    def __init__(self, account, driver):
        self.driver = driver
        self.account = account
        self.username = account.username
        self.password = account.password
        self.is_logged_in = False
        self.login_url = "https://lobby.ogame.gameforge.com/de_DE/?language=de"
        self.base_login_url = 'https://s158-de.ogame.gameforge.com'
        self.report = {}

    def goto(self, view_id="", planet_id=""):
        if not self.is_logged_in:
            self.login()

        self.driver.get(self.base_login_url + '/game/index.php?page=' + view_id + '&cp=' + planet_id)

    def login(self):
        self.driver.get(self.login_url)
        assert "OGame" in self.driver.title
        self.driver.find_element_by_id("ui-id-1").click()
        self.driver.find_element_by_id("usernameLogin").send_keys(self.username)
        self.driver.find_element_by_id("passwordLogin").send_keys(self.password)
        self.driver.find_element_by_id("loginSubmit").click()
        WebDriverWait(self.driver, 15).until(EC.title_is("OGame Lobby"))
        self.driver.find_element_by_css_selector("button.button.button-default").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 15).until(EC.title_is("Fenrir OGame"))
        self.is_logged_in = True
