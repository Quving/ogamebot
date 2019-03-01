from bot.services import helper
from bot.services.interactor import Interactor
from inventory.models import Inventory
from mine.models import MetalMine, DeuteriumMine, CrystalMine, SolarPowerstation, FusionReactor, SolarSatellite
from planet.models import Planet, Coordinate


class Crawler(Interactor):
    def __init__(self, account, driver, logger=None):
        Interactor.__init__(self, account, driver, logger=logger)

    def crawl(self):
        """
        Initializes the crawling process. Crawls everything.
        :return:
        """
        if not self.is_logged_in:
            self.login()

        playername = self.crawl_playername()

        self.account.playername = playername
        self.account.save()

        planet_ids, planet_names = self.crawl_planets()

        report = {}

        for (planet_id, planet_name) in zip(planet_ids, planet_names):
            # Create planet object
            self.logger.info("Crawl planet {} (id={}).".format(planet_name, planet_id))
            x, y, z = helper.get_coords_from_planet_name(planet_name)
            planet_coord, created = Coordinate.objects.get_or_create(
                x=x,
                y=y,
                z=z
            )

            if Planet.objects.filter(id=planet_id).exists():
                planet = Planet.objects.get(id=planet_id)
            else:
                self.logger.info("New planet {} registered and will be added to db.".format(planet_name))
                planet = Planet(
                    id=planet_id,
                    name=planet_name,
                    account=self.account,
                    coord=planet_coord
                )
                planet.save()

            report[planet_id] = {"main": False}
            report[planet_id]["resources"] = self.crawl_mines(planet)
            report[planet_id]["inventory"] = self.crawl_inventory(planet)

            # Set first planet as main
            report[planet_ids[0]]["main"] = True
            self.report = report

    def crawl_playername(self):
        if not self.is_logged_in:
            self.login()

        playername = self.driver.find_element_by_css_selector("#playerName span").text
        return playername

    def crawl_planets(self):
        """
        Crawls the planet_ids and stores them in the attributes.
        :return:
        """
        if not self.is_logged_in:
            self.login()

        planet_css = self.driver.find_elements_by_css_selector("#planetList .smallplanet")
        planet_names_css = self.driver.find_elements_by_css_selector("#planetList .smallplanet .planet-name")
        planet_ids, planet_names = [], []

        for (planet_css, planet_name_css) in zip(planet_css, planet_names_css):
            id_complete = planet_css.get_attribute("id")
            id_str = "".join([s for s in id_complete if s.isdigit()])
            name_str = planet_css.text
            planet_ids.append(int(id_str))
            planet_names.append(name_str.strip().replace("\n", ""))

        return planet_ids, planet_names

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
