import time

from pages.page_base import PageBase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.common import Common


class HomePage(PageBase):

    def __init__(self, driver, logger):
        super(HomePage, self).__init__(driver, logger)
        self.town_element_path = "//a[@href='PendPostbyTownDetails.aspx?town={}']"
        self.pending_forecloser_sales_table = (By.XPATH, "//table[@id='ctl00_cphBody_GridView1']/tbody/tr")
        self.click_back_to_towns = (By.ID, "ctl00_cphBody_hlnktownlist")
        self.common = Common(self.logger)

    def click_town(self, name):
        return self.driver_utility.click_element((By.XPATH, self.town_element_path.format(name)))

    def navigate_to_home_page(self):
        self.driver_utility.click_element(self.click_back_to_towns)

    def get_town_forecloser_entries_older_than_n_days(self, days_old):
        elements = self.driver_utility.get_all_elements(self.pending_forecloser_sales_table)
        table_id = self.driver.find_element(By.ID, 'ctl00_cphBody_GridView1')
        rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        self.logger.info("Total rows {}".format(len(rows)))
        if len(elements) == 1:
            return False
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")  # note: index start from 0, 1 is col 2
            self.logger.info(cols[1].text)
            if self.common.check_diff_days(cols[1].text, days_old):
                self.logger.info("Click View Full notice")
                view_ele = row.find_element(By.XPATH, '//a[text()="View Full Notice"]').send_keys(
                    Keys.CONTROL + Keys.RETURN)
                time.sleep(3)
        self.navigate_to_home_page()
