import os.path
import unittest
import logging as SystemLogging
import sys
from datetime import datetime
from selenium import webdriver
import yaml
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.towns.homepage import HomePage


class UITestBase(unittest.TestCase):
    SystemLogging.StreamHandler(sys.stdout)
    SystemLogging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                              level=SystemLogging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging = SystemLogging

    @classmethod
    def setUpClass(cls) -> None:
        formatter = SystemLogging.Formatter('%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        cls.logging.getLogger().handlers[0].setFormatter(formatter)
        cls.test_start_time = datetime.now()
        cls.test_end_time = datetime.now()
        cls.logging.info("CLASS LEVEL INITIALIZATION")
        current_path = os.path.abspath(os.path.dirname(__file__))
        config_path = current_path + "/../config/config.yaml"
        yaml_dict = ""
        with open(config_path, 'r') as yaml_fh:
            yaml_dict = yaml.load(yaml_fh)
        cls.config_dict = yaml_dict
        cls.logging.info(yaml_dict)

        cls.baseURL = cls.config_dict['base_url']
        cls.driver = cls.initialize_webdriver()
        cls.driver.implicitly_wait(cls.config_dict['implicit_webdriver_timeout'])
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.get(cls.baseURL)
        cls.logging.info("Navigated to base url [ {} ] ".format(cls.baseURL))

        # Page Objects
        cls.home_page = HomePage(cls.driver, cls.logging)

    def setUp(self) -> None:
        now = datetime.now()
        date_str = now.strftime("%d/%m/%y %H:%M:%S")
        self.logging.info("Test execution started [ {} ] at [{}]".format(self._testMethodName,
                                                                         date_str))
        self.test_start_time = datetime.now()

    def tearDown(self) -> None:
        self.logging.info("***** Test END *****")
        self.driver.close()

    @classmethod
    def initialize_webdriver(cls):
        default_browser = 'chrome'
        cls.driver_path = cls.config_dict['chrome_driver_path']
        # TODO based on configuration we can swith to different browsers
        if default_browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_experimental_option('w3c', False)
        driver = webdriver.Chrome(executable_path=cls.driver_path,
                                  chrome_options=options, desired_capabilities=DesiredCapabilities.CHROME)
        driver.set_window_size(1366, 768, driver.window_handles[0])
        return driver
