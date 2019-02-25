import time

from bot.services.interactor import Interactor


class Stacker(Interactor):
    def __init__(self, account, driver, logger=None):
        Interactor.__init__(self, account, driver, logger=logger)

    def stack(self):
        if not self.is_logged_in:
            self.login()

        planet_main = self.account.planets.get(is_main=True)
        for planet in self.account.planets.filter(is_main=False):
            self.goto(view_id='fleet1', planet_id=planet.id)

            # If ships are available.
            if self.driver.find_element_by_css_selector('#button203').get_attribute('class') == 'on':
                self.driver.find_element_by_css_selector("#ship_203").send_keys("10")

                # Continue if possible
                next_btn = self.driver.find_element_by_css_selector('#continue')
                if next_btn.get_attribute("class") == 'on':
                    next_btn.click()

                    time.sleep(3)
                    self.driver.find_element_by_css_selector('.coords #position').send_keys(planet_main.coord.z)
                    self.driver.find_element_by_css_selector('.coords #system').send_keys(planet_main.coord.y)
                    x = self.driver.find_element_by_css_selector('.coords #galaxy')
                    x.clear()
                    x.send_keys(planet_main.coord.x)
                    time.sleep(3)

                # Continue if possible
                next_btn = self.driver.find_element_by_css_selector('#steps #continue')
                if next_btn.get_attribute("class") == 'on':
                    next_btn.click()
                    self.driver.find_element_by_css_selector('#missionButton3').click()
                    self.driver.find_element_by_css_selector('#allresources').click()
                    time.sleep(3)

                # Send if possible
                next_btn = self.driver.find_element_by_css_selector('#start')
                if next_btn.get_attribute("class") == 'on':
                    next_btn.click()
                    time.sleep(5)
                    self.logger.info("Send fleet to {}".format(planet_main.name))
            else:
                self.logger.info("Planet {} is not avaiable for stacking ressources.".format(planet.name))
