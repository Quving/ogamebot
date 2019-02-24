import time

from bot.services.interactor import Interactor


class Stacker(Interactor):
    def __init__(self, account, driver):
        Interactor.__init__(self, account, driver)

    def stack(self):
        if not self.is_logged_in:
            self.login()

        planet_main = self.account.planets.filter(is_main=True)[0]
        for planet in self.account.planets.filter(is_main=False):
            self.goto(view_id='fleet1', planet_id=planet.id)
            self.driver.find_element_by_css_selector("#ship_203").send_keys("5")

            # Continue if possible
            next_btn = self.driver.find_element_by_css_selector('#continue')
            if next_btn.get_attribute("class") == 'on':
                next_btn.click()

                time.sleep(1)
                self.driver.find_element_by_css_selector('.coords #position').send_keys(planet_main.coord.z)
                self.driver.find_element_by_css_selector('.coords #system').send_keys(planet_main.coord.y)
                x = self.driver.find_element_by_css_selector('.coords #galaxy')
                x.clear()
                x.send_keys(planet_main.coord.x)
                time.sleep(1)

            # Continue if possible
            next_btn = self.driver.find_element_by_css_selector('#steps #continue')
            if next_btn.get_attribute("class") == 'on':
                next_btn.click()
                self.driver.find_element_by_css_selector('#missionButton3').click()
                self.driver.find_element_by_css_selector('#allresources').click()
                time.sleep(1)

            # Send if possible
            next_btn = self.driver.find_element_by_css_selector('#start')
            if next_btn.get_attribute("class") == 'on':
                next_btn.click()
                time.sleep(5)
                print("SEND")


