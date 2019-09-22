import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa.settings import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_BROWSER_POSITION
from qa.settings import HOST_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH
from qa.settings import APPIUM_HUB
# from appium import webdriver as appiumdriver


def dict_from_string(current_dict, string):
    for item in string.split(','):
        key, value = item.split(':')
        current_dict[key.strip(' \"}{:')] = value.strip(' \"}{:')
    return current_dict




class Browser(object):


    # def __init__(self):
    def __init__(self, **kwargs):
        print('Loading normal browser list')
        # if kwargs is not None:
        #     self.bearer_header = kwargs['bearer_header']
        #

    def set_defaults(self, browser_obj):
        browser_obj.set_window_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        # Keep position 2nd or Safari will reposition on set_window_sizeself
        # Safari also requires you account for OSX Top Nav & is iffy about edge
        browser_obj.set_window_position(
            DEFAULT_BROWSER_POSITION['x'],
            DEFAULT_BROWSER_POSITION['y']
        )


    def mandatory_chrome_options(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api"
        )
        return self.chrome_options


    def generic_chrome_dc(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.desired_capabilities['acceptInsecureCerts'] = True
        return self.desired_capabilities


    def setup_firefox_dc(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.desired_capabilities['acceptInsecureCerts'] = True
        # self.desired_capabilities['javascriptEnabled'] = True
        return self.desired_capabilities


    def get_chrome_driver(self):
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_headless_chrome(self):
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
        # self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            options=self.chrome_options,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_remote_headless_chrome(self):
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
        # self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            options=self.chrome_options,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_remote_chrome(self):
        # self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        # https://stackoverflow.com/questions/50642308/org-openqa-selenium-webdriverexception-unknown-error-devtoolsactiveport-file-d
        self.desired_capabilities = {
          'browserName': 'chrome',
          'chromeOptions':  {
            'useAutomationExtension': False,
            'forceDevToolsScreenshot': True,
            'args': ['--disable-plugins', '--disable-instant-extended-api']
          }
        }
        # self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument(
        #     "--disable-plugins --disable-instant-extended-api")
        # self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )

        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_last_headless_chrome(self):
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.desired_capabilities['browerVersion'] = '76.0.3809'
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_remote_last_chrome(self):
        # self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        # self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        # self.desired_capabilities['browerVersion'] = '76.0.3809'
        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument(
        #     "--disable-plugins --disable-instant-extended-api")
        # self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.desired_capabilities = {
            'browserName': 'chrome',
            'browerVersion': '76.0.3809',
            'chromeOptions':  {
                'useAutomationExtension': False,
                'forceDevToolsScreenshot': True,
                'args': ['--disable-plugins', '--disable-instant-extended-api']
            }
        }
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )

        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_local_ga_chrome(self):
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.add_extension(
            '%senv/bin/ga_tracker.crx' % QA_FOLDER_PATH)
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.browser


    def get_remote_ga_chrome(self):
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
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


    def get_local_html_validator(self):
        # Can't have normal --disable-plugins flag 
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.add_extension(
            '%sutilities/html_validator/Validity.crx' % QA_FOLDER_PATH)

        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.browser

    def get_remote_html_validator(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
        self.dir = os.path.dirname(__file__)
        self.path = os.path.join(
            self.dir, '../../../qa/utilities/html_validator/Validity.crx')
        self.chrome_options.add_extension(self.path)
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        return self.browser


    def get_firefox_driver(self):
        self.desired_capabilities = self.setup_firefox_dc()
        self.browser = webdriver.Firefox(
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_headless_firefox_driver(self):
        self.desired_capabilities = self.setup_firefox_dc()
        options = FirefoxOptions()
        options.headless = True
        # get a driver on the proxy
        self.browser = webdriver.Firefox(
            desired_capabilities=self.desired_capabilities,
            options=options
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_remote_firefox_driver(self):
        self.desired_capabilities = self.setup_firefox_dc()
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        self.set_defaults(self.browser)
        return self.browser


    def get_last_remote_firefox_driver(self):
        self.desired_capabilities = self.setup_firefox_dc()
        self.desired_capabilities['browerVersion'] = '68.1.0'
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        self.set_defaults(self.browser)
        return self.browser


    def get_safari_driver(self):
        self.browser = webdriver.Safari()
        # SETTING set_window_size BREAKS Safari at certain versions, Poistioning helps
        # look for bug and version if its crashing.
        # self.set_defaults(self.browser)
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
        # self.set_defaults(self.browser)
        return self.browser


    def return_driver_dict(self):
        self.drivers = {
            'chrome': self.get_chrome_driver,
            'custom_device': self.get_custom_emulation,
            'firefox': self.get_firefox_driver,
            'ga_chrome': self.get_local_ga_chrome,
            'last_headless_chrome': self.get_last_headless_chrome,
            'last_remote_firefox': self.get_last_remote_firefox_driver,
            'local_html_validator': self.get_local_html_validator,
            'headless_chrome': self.get_headless_chrome,
            'headless_firefox': self.get_headless_firefox_driver,
            'mobile_galaxy_s8': self.get_galaxy_s8_emulation,
            'mobile_iphone_7': self.get_iphone_7_emulation,
            'mobile_nexus_5x': self.get_nexus_5x_emulation,
            'remote_chrome': self.get_remote_chrome,
            'remote_headless_chrome': self.get_remote_headless_chrome,
            'remote_last_chrome': self.get_remote_last_chrome,
            'remote_firefox': self.get_remote_firefox_driver,
            'remote_ga_chrome': self.get_remote_ga_chrome,
            'remote_html_validator': self.get_remote_html_validator,
            'remote_safari': self.get_remote_safari_driver,
            'safari': self.get_safari_driver,
            'saucelabs': self.get_sauce_driver
        }
        return self.drivers


    def get_browser_driver(self):
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            raise EnvironmentError('Unrecognized driver: %s' % DRIVER)
        else:
            return drivers.get(DRIVER)()


    def get_driver_by_name(self, name):
        print('Getting Custom Driver: %s' % name)
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            raise EnvironmentError('Unrecognized driver: %s' % DRIVER)
        else:
            return drivers.get(name)()
