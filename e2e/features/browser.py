from selenium import webdriver
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH


def dict_from_string(current_dict, string):
    for item in string.split(','):
        key, value = item.split(':')
        current_dict[key.strip(' \"}{:')] = value.strip(' \"}{:')
    return current_dict


def set_defaults(browser_obj):
    browser_obj.set_window_position(0, 0)
    browser_obj.set_window_size(1366, 768)


class Browser(object):

    def get_chrome_driver(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api")

        self.desired_capabilities.update(self.chrome_options.to_capabilities())

        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )

        # Desktop size
        set_defaults(self.browser)
        return self.browser

    def get_headless_chrome(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api \
            --headless")

        self.desired_capabilities.update(self.chrome_options.to_capabilities())

        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )

        # Desktop size
        set_defaults(self.browser)
        return self.browser

    def get_firefox_driver(self):

        self.browser = webdriver.Firefox()

        # Desktop size
        set_defaults(self.browser)
        return self.browser

    def get_remote_firefox_driver(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.desired_capabilities['acceptInsecureCerts'] = True
        self.desired_capabilities['javascriptEnabled'] = True

        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )

    def get_safari_driver(self):

        self.browser = webdriver.Safari()
        # SETTING WIDTH HERE BREAKS SAFARI
        # set_defaults(browser)
        return self.browser

    def get_remote_safari_driver(self):
        # For use with selenium hub
        self.desired_capabilities = webdriver.DesiredCapabilities.SAFARI
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.desired_capabilities['maxInstances'] = 1
        self.desired_capabilities['maxSession'] = 1
        self.desired_capabilities['acceptSslCerts'] = True
        # desired_capabilities['useTechnologyPreview'] = True
        self.desired_capabilities['useCleanSession'] = True

        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )

        return self.browser

    def get_sauce_driver(self):
        # For use with selenium hub
        self.desired_capabilities = {}
        self.desired_capabilities = dict_from_string(
            self.desired_capabilities, SL_DC)
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        return self.browser

    def return_driver_dict(self):
        self.drivers = {
            'chrome': self.get_chrome_driver,
            'firefox': self.get_firefox_driver,
            'remote_firefox': self.get_remote_firefox_driver,
            'headless_chrome': self.get_headless_chrome,
            'safari': self.get_safari_driver,
            'remote_safari': self.get_remote_safari_driver,
            'saucelabs': self.get_sauce_driver
        }
        return self.drivers

    def get_browser_driver(self):
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(DRIVER)()
