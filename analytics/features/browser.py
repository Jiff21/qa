from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH

DRIVER = 'chrome'


class Browser(object):

    def get_chrome_driver(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_extension(
            '%senv/bin/ga_tracker.crx' % QA_FOLDER_PATH)
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

        return self.driver

    def return_driver_dict(self):
        self.drivers = {
            'chrome': self.get_chrome_driver,
        }
        return self.drivers

    def get_browser_driver(self):
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(DRIVER)()
