from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class DriverUtility:

    def __init__(self, driver, logger, timeout):
        self.driver = driver
        self.timeout = timeout
        self.logger = logger

    def get_element(self, bylocator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(bylocator))
        return element

    def get_all_elements(self, bylocator):
        elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(bylocator))
        return elements

    def scroll_down(self, value):
        self.driver.execute_script("window.scrollBy(0,{})".format(str(value)))

    def click_element(self, bylocator):
        scrolls = 0
        no_of_scrolls = 4
        while scrolls < no_of_scrolls:
            try:
                element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(bylocator))
                time.sleep(1)
                element.click()
                time.sleep(3)
                return True
            except Exception as ex:
                scrolls += 1
                self.logger.info("**** EXCEPTION **** {}".format(scrolls))
                self.scroll_down(300)
        return False
