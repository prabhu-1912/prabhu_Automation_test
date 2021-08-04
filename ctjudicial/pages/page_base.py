from common.driver_utility import DriverUtility


class PageBase():
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.driver_utility = DriverUtility(self.driver, logger, 5)
