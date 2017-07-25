from selenium import webdriver
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH
from selenium.webdriver.chrome.options import Options


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
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument("--window-position=0,0")
        # self.chrome_options.add_argument("--headless")

        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )

        set_defaults(self.browser)
        return self.browser

    def get_mobile_chrome(self):
        mobile_emulation = {
            # 'deviceName': 'Nexus 5X'
            # 'deviceName': 'Nexus 6P'
            # 'deviceName': 'Nexus 7'
            # 'deviceName': 'iPhone 5'
            # 'deviceName': 'iPhone 6 Plus'
            # 'deviceName': 'iPad Pro'
            'deviceName': 'Galaxy S5'
            # Or specify a specific build using the following two arguments
            #"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
            #"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        }
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option(
            "mobileEmulation", mobile_emulation)
        # self.chrome_options.add_argument("--headless")

        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )

        # set_defaults(self.browser)
        return self.browser

    def get_firefox_driver(self):

        self.browser = webdriver.Firefox()

        # Desktop size
        set_defaults(self.browser)
        return self.browser

    def return_driver_dict(self):
        self.drivers = {
            'chrome': self.get_chrome_driver,
            'firefox': self.get_firefox_driver,
            'headless_chrome': self.get_headless_chrome,
            'mobile_chrome': self.get_mobile_chrome

        }
        return self.drivers

    def get_browser_driver(self):
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(DRIVER)()
