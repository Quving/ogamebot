import json
import os
import platform

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def toJson(data):
    with open("becks.json", "w") as file:
        file.write(json.dumps(data, ensure_ascii=False, indent=4))


class Crawler:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False
        self.login_url = "https://lobby.ogame.gameforge.com/de_DE/?language=de"
        self.base_login_url = 'https://s158-de.ogame.gameforge.com'
        self.report = {}
        if platform.system() == "Darwin":
            options = webdriver.ChromeOptions()
            options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
            self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)

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

    def crawl(self):
        """
        Initializes the crawling process. Crawls everything.
        :return:
        """
        if not self.is_logged_in:
            self.login()
        planet_ids = self.crawl_planet_ids()
        report = {}

        for planet_id in planet_ids:
            report[planet_id] = {"main": False}
            report[planet_id]["resources"] = self.crawl_resources(planet_id)
            report[planet_id]["inventory"] = self.crawl_inventory(planet_id)

        # Set first planet as main
        report[planet_ids[0]]["main"] = True
        self.report = report

    def crawl_planet_ids(self):
        """
        Crawls the planet_ids and stores them in the attributes.
        :return:
        """
        if not self.is_logged_in:
            self.login()
        planets_css = self.driver.find_elements_by_css_selector("#planetList .smallplanet")
        planet_ids = []
        for planet_css in planets_css:
            id_complete = planet_css.get_attribute("id")
            id_str = "".join([s for s in id_complete if s.isdigit()])
            planet_ids.append(id_str)

        return planet_ids

    def crawl_inventory(self, planet_id):
        """
        Crawls the planets inventory (metal, crystal, darkmatter energy)
        and stores it as class attribute 'inventory_report'.
        """
        if not self.is_logged_in:
            self.login()

        inventory_report = dict()
        resource_metal = self.driver.find_element_by_id('resources_metal').text
        resource_crystal = self.driver.find_element_by_id('resources_crystal').text
        resource_deuterium = self.driver.find_element_by_id('resources_deuterium').text
        resource_darkmatter = self.driver.find_element_by_id('resources_darkmatter').text
        resource_energy = self.driver.find_element_by_id('resources_energy').text

        inventory_report[planet_id] = {
            "metal": float(resource_metal),
            "crystal": float(resource_crystal),
            "deuterium": float(resource_deuterium),
            "darkmatter": float(resource_darkmatter),
            "energy": float(resource_energy)
        }

        return inventory_report

    def crawl_resources(self, planet_id):
        """
        Crawls the planets' resources (mines) and stores them as class attribute 'resource_report'."
        :return:
        """
        if not self.is_logged_in:
            self.login()
        resource_ids = ["iron_mine",
                        "crystal_mine",
                        "deuterium_mine",
                        "solar_power_station",
                        "fusion_reactor",
                        "solar_satellite"]
        self.goto(view_id="resources", planet_id=planet_id)

        resource_report = dict()
        for i in range(1, 7):
            resource_name = resource_ids[i - 1]
            upgradeable_css = "#button{}".format(i)
            level_css = "#button{} .level".format(i)
            level = self.driver.find_element_by_css_selector(level_css).text
            upgradeable = self.driver.find_element_by_css_selector(upgradeable_css).get_attribute("class") == "on"

            resource_report[resource_name] = {
                "level": level,
                "upgradeable": upgradeable
            }
        return resource_report

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    username, password = os.getenv("OGAME_USERNAME"), os.getenv("OGAME_PASSWORD")
    crawler = Crawler(username=username, password=password)
    crawler.crawl()
    toJson(crawler.report)
    crawler.quit()
