import pytest
from common.uitestbase import UITestBase
import time


class TestSales(UITestBase):

    @pytest.mark.p0
    def test_town_sale_within_n_days(self):
        towns = ['Trumbull','Norwalk', 'Stamford','Shelton','Fairfield']
        # towns = ['Milford%C2%A0%C2%A0']
        self.logging.info(self.config_dict['browser'])
        for each_town in towns:
            self.logging.info("Verifying sales details for {} ".format(each_town))
            if not self.home_page.click_town(each_town):
                self.logging.info("Town {} not found in sales ".format(each_town))
            else:
                time.sleep(3)
                self.home_page.get_town_forecloser_entries_older_than_n_days(days_old=self.config_dict['number_of_days_diff_records'])
