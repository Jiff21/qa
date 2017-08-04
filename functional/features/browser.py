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

    def get_galaxy_s8_emulation(self):
        self.device = {
            'deviceMetrics': {'width': 1440, 'height': 2960, 'pixelRatio': 4.0},
            'userAgent': 'mozilla/5.0 (Linux; Android 7.0; \
            SM-G892A Build/NRD90M applewebkit/537.36 (KHTML, like Gecko) \
            Chrome/56.0.2924.87 Mobile Safari/537.36'
        }
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option(
            "mobileEmulation", self.device)
        # self.chrome_options.add_argument("--headless")

        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )
        return self.browser

    def get_nexus_5x_emulation(self):
        self.device = {
            'deviceMetrics': {'width': 1080, 'height': 1920, 'pixelRatio': 2.6},
            'userAgent': 'mozilla/5.0 (Linux; Android 6.0.1; \
            Nexus 5x build/mtc19t applewebkit/537.36 (KHTML, like Gecko) \
            Chrome/51.0.2702.81 Mobile Safari/537.36'
        }
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option(
            "mobileEmulation", self.device)
        # self.chrome_options.add_argument("--headless")

        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )
        return self.browser

    def get_iphone_7_emulation(self):
        self.device = {
            'deviceMetrics': {'width': 750, 'height': 1334, 'pixelRatio': 2.0},
            'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) \
            AppleWebKit/602.4.6 (KHTML, like Gecko) \
            Version/10.0 Mobile/14D27 Safari/602.1'
        }
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option(
            "mobileEmulation", self.device)
        # self.chrome_options.add_argument("--headless")

        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )
        return self.browser

    def get_custom_emulation(self):
        custom_device = {
            'deviceMetrics': {'width': 360, 'height': 640, 'pixelRatio': 3.0},
            'userAgent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 \
            Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) \
            Chrome/18.0.1025.166 Mobile Safari/535.19'
        }
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option(
            "mobileEmulation", custom_device)
        # self.chrome_options.add_argument("--headless")

        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )

        # set_defaults(self.browser)
        return self.browser

    def return_driver_dict(self):
        self.drivers = {
            'chrome': self.get_chrome_driver,
            'custom_device': self.get_custom_emulation,
            'firefox': self.get_firefox_driver,
            'galaxy_s8': self.get_galaxy_s8_emulation,
            'headless_chrome': self.get_headless_chrome,
            'iphone_7': self.get_iphone_7_emulation,
            'nexus_5x': self.get_nexus_5x_emulation,
            'remote_firefox': self.get_remote_firefox_driver,
            'remote_safari': self.get_remote_safari_driver,
            'safari': self.get_safari_driver,
            'saucelabs': self.get_sauce_driver
        }
        return self.drivers

    def get_browser_driver(self):
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(DRIVER)()
