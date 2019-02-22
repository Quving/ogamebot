from bot.services.interactor import Interactor
import time

class Stacker(Interactor):
    def __init__(self, account, driver):
        Interactor.__init__(self, account, driver)

    def stack(self):
        if not self.is_logged_in:
            self.login()

        planet_main = self.account.planets.get(is_main=True)

        for planet in self.account.planets.filter(is_main=False):
           self.goto(view_id='fleet1', planet_id=planet.id)
           time.sleep(5)


