import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH


class Browser(object):

    def get_chrome_driver(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_extension(
            '%senv/bin/ga_tracker.crx' % QA_FOLDER_PATH)
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

        return self.driver

    def get_gitlab_chrome(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api \
            --headless")
        self.dir = os.path.dirname(__file__)
        self.path = os.path.join(
            self.dir, '../../../qa/analytics/ga_tracker.crx')
        self.chrome_options.add_extension(self.path)
        self.desired_capabilities.update(self.chrome_options.to_capabilities())

        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )

        return self.browser

    def return_driver_dict(self):
        self.drivers = {
            'chrome': self.get_chrome_driver,
            'gitlab_chrome': self.get_gitlab_chrome
        }
        return self.drivers

    def get_browser_driver(self):
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(DRIVER)()
