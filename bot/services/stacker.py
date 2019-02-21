from bot.services.interactor import Interactor


class Stacker(Interactor):
    def __init__(self, account, driver):
        Interactor.__init__(self, account, driver)
