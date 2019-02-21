import json
import platform

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from account.models import Account
from inventory.models import Inventory
from mine.models import MetalMine, DeuteriumMine, CrystalMine, SolarPowerstation, FusionReactor, SolarSatellite
from planet.models import Planet


class MyWebdriver:
    def __init__(self, remote=True):
        if not remote and platform.system() == "Darwin":
            options = webdriver.ChromeOptions()
            options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
            self.driver = webdriver.Chrome(chrome_options=options)
        else:
            selenium_hub_host = "http://grapefruit.quving.com:4444"
            selenium_hub_url = selenium_hub_host + "/wd/hub"
            self.driver = webdriver.Remote(command_executor=selenium_hub_url,
                                           desired_capabilities={'browserName': 'firefox'})
        self.driver.implicitly_wait(10)


class Crawler:
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
            # Create planet object
            planet, created = Planet.objects.get_or_create(
                id=planet_id,
                account=self.account
            )
            planet.save()

            report[planet_id] = {"main": False}
            report[planet_id]["resources"] = self.crawl_mines(planet)
            report[planet_id]["inventory"] = self.crawl_inventory(planet)
            planet.save()

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

    def crawl_inventory(self, planet):
        """
        Crawls the planets inventory (metal, crystal, darkmatter energy)
        and stores it as class attribute 'inventory_report'.
        """
        planet_id = planet.id
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

        inventory, created = Inventory.objects.get_or_create(planet=planet,
                                                             metal=resource_metal,
                                                             crystal=resource_crystal,
                                                             deuterium=resource_deuterium,
                                                             dark_matter=resource_darkmatter,
                                                             energy=resource_energy)
        inventory.save()
        return inventory_report

    def crawl_mines(self, planet):
        """
        Crawls the planets' resources (mines) and stores them as class attribute 'resource_report'."
        :return:
        """
        planet_id = planet.id
        if not self.is_logged_in:
            self.login()

        resource_ids = ["MetalMine", "CrystalMine", "DeuteriumMine",
                        "SolarPowerstation", "FusionReactor", "SolarSatellite"]
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
            if i == 1:
                mine, created = MetalMine.objects.get_or_create(planet=planet,
                                                                upgradeable=upgradeable,
                                                                name=resource_name,
                                                                level=level)
            elif i == 2:
                mine, created = CrystalMine.objects.get_or_create(planet=planet,
                                                                  upgradeable=upgradeable,
                                                                  name=resource_name,
                                                                  level=level)
            elif i == 3:
                mine, created = DeuteriumMine.objects.get_or_create(planet=planet,
                                                                    upgradeable=upgradeable,
                                                                    name=resource_name,
                                                                    level=level)
            elif i == 4:
                mine, created = SolarPowerstation.objects.get_or_create(planet=planet,
                                                                        upgradeable=upgradeable,
                                                                        name=resource_name,
                                                                        level=level)
            elif i == 5:
                mine, created = FusionReactor.objects.get_or_create(planet=planet,
                                                                    upgradeable=upgradeable,
                                                                    name=resource_name,
                                                                    level=level)
            else:
                mine, created = SolarSatellite.objects.get_or_create(planet=planet,
                                                                     upgradeable=upgradeable,
                                                                     name=resource_name,
                                                                     level=level)
            mine.save()
        return resource_report


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
