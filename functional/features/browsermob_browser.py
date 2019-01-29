import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from qa.functional.features.browser import Browser as NormalBrowser
from qa.settings import DEFAULT_WIDTH, DEFAULT_HEIGHT
from qa.settings import DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH
from qa.utilities.mod_header.custom_headers import create_modheaders_plugin
from qa.utilities.oauth.service_account_auth import make_iap_request
from qa.utilities.oauth.safari_proxy import SafariProxy



def dict_from_string(current_dict, string):
    for item in string.split(','):
        key, value = item.split(':')
        current_dict[key.strip(' \"}{:')] = value.strip(' \"}{:')
    return current_dict



def set_defaults(browser_obj):
    browser_obj.set_window_position(10, 30)
    browser_obj.set_window_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)



class Browser(object):


    def __init__(self, bearer_header=None, proxy=None, server=None, **kwargs):
        print ('Setting up Browsermob Browser List')
        self.normal_browser = NormalBrowser()
        self.bearer_header = bearer_header
        self.proxy = proxy
        self.server = server


    def get_authenticated_chrome_driver(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--proxy-server=%s' % self.proxy.proxy)
        # other chrome options
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api"
        )
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        # Get a WebDriver instance
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )
        set_defaults(self.browser)
        return self.browser


    def get_remote_authenticated_chrome_driver(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--proxy-server=%s' % self.proxy.proxy)
        # other chrome options
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api"
        )
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        # Get a WebDriver instance
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        set_defaults(self.browser)
        return self.browser


    def get_headless_authenticated_chrome_driver(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--proxy-server=%s' % self.proxy.proxy)
        # other chrome options
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api --headless"
        )
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        # Get a WebDriver instance
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        set_defaults(self.browser)
        return self.browser


    def get_authenticated_local_ga_chrome(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--proxy-server=%s' % self.proxy.proxy)
        # other chrome options\
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options.add_extension(
            '%senv/bin/ga_tracker.crx' % QA_FOLDER_PATH
        )
        # Get a WebDriver instance
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.driver


    def get_authenticated_remote_ga_chrome(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--proxy-server=%s' % self.proxy.proxy)
        # other chrome options\
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api \
            --headless"
        )
        self.dir = os.path.dirname(__file__)
        self.path = os.path.join(
            self.dir, '../../../qa/analytics/ga_tracker.crx')
        self.chrome_options.add_extension(self.path)
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        # Get a WebDriver instance
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        return self.browser


    def get_authenticated_local_html_validator(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--proxy-server=%s' % self.proxy.proxy)
        # other chrome options\
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.chrome_options.add_extension(
            '%sutilities/html_validator/Validity.crx' % QA_FOLDER_PATH
        )
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.driver


    def get_authenticated_remote_html_validator(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--proxy-server=%s' % self.proxy.proxy)

        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api \
            --headless"
        )
        self.dir = os.path.dirname(__file__)
        self.path = os.path.join(
            self.dir, '../../../qa/utilities/html_validator/Validity.crx'
        )
        self.chrome_options.add_extension(self.path)
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        return self.browser



    def get_auth_firefox_driver(self):
        profile  = webdriver.FirefoxProfile()
        profile.set_proxy(self.proxy.selenium_proxy())
        # get a driver on the proxy
        self.browser = webdriver.Firefox(firefox_profile=profile)
        # Desktop size
        set_defaults(self.browser)
        return self.browser



    def get_headless_auth_firefox_driver(self):
        options = FirefoxOptions()
        options.headless = True
        # Add Bearer headers to browsermob proxy
        profile  = webdriver.FirefoxProfile()
        profile.set_proxy(self.proxy.selenium_proxy())
        # get a driver on the proxy
        self.browser = webdriver.Firefox(
            firefox_profile=profile,
            options=options
        )
        # Desktop size
        set_defaults(self.browser)
        return self.browser


    def get_remote_authenticated_firefox_driver(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.desired_capabilities['acceptInsecureCerts'] = True
        self.desired_capabilities['javascriptEnabled'] = True
        profile  = webdriver.FirefoxProfile()
        profile.set_proxy(self.proxy.selenium_proxy())
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            browser_profile=profile,
            desired_capabilities=self.desired_capabilities
        )
        return self.browser



    def get_auth_safari_driver(self):
        # other safari options
        # print(self.server.host)
        # print(self.proxy.port)
        self.safari_proxy = SafariProxy(self.server.host, self.proxy.port)
        self.desired_capabilities = webdriver.DesiredCapabilities.SAFARI
        # Returns "SessionNotCreatedException: Message: Capability 'acceptInsecureCerts' could not be honored."
        # self.desired_capabilities['acceptSslCerts'] = True
        self.desired_capabilities['safari.options'] = {
            # 'webSecurityEnabled': False,
            'cleanSession': True,
            'technologyPreview': True
        }
        # SessionNotCreatedException: Message: Capability 'proxy' could not be honored.
        # https://w3c.github.io/webdriver/#proxy
        # self.desired_capabilities['proxy'] = {
        #     'httpProxy': self.proxy.proxy,
        #     'ftpProxy': self.proxy.proxy,
        #     'sslProxy': self.proxy.proxy,
        #     'noProxy': [],
        #     'proxyType': "MANUAL",
        # }
        self.browser = webdriver.Safari(
            desired_capabilities=self.desired_capabilities,
            executable_path='/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver'
        )
        self.safari_proxy.on()
        # opens 2?
        self.browser = webdriver.Safari(
            desired_capabilities=self.desired_capabilities
        )
        # Opens 1 but wrong
        # self.browser = webdriver.Safari()
        # process.wait()
        print(self.desired_capabilities)
        # set_defaults(browser)
        return self.browser



    def return_driver_dict(self):
        self.drivers = {
            'chrome': self.normal_browser.get_chrome_driver,
            'ga_chrome': self.normal_browser.get_local_ga_chrome,
            'remote_ga_chrome': self.normal_browser.get_remote_ga_chrome,
            'local_html_validator': self.normal_browser.get_local_html_validator,
            'remote_html_validator': self.normal_browser.get_remote_html_validator,
            'remote_firefox': self.normal_browser.get_remote_firefox_driver,
            'firefox': self.normal_browser.get_firefox_driver,
            'headless_chrome': self.normal_browser.get_headless_chrome,
            'headless_firefox': self.normal_browser.get_headless_firefox_driver,
            'safari': self.normal_browser.get_safari_driver,
            'custom_device': self.normal_browser.get_custom_emulation,
            'galaxy_s8': self.normal_browser.get_galaxy_s8_emulation,
            'iphone_7': self.normal_browser.get_iphone_7_emulation,
            'nexus_5x': self.normal_browser.get_nexus_5x_emulation,
            'saucelabs': self.normal_browser.get_sauce_driver,
            'remote_safari': self.normal_browser.get_remote_safari_driver,
            'authenticated_chrome': self.get_authenticated_chrome_driver,
            'authenticated_firefox': self.get_auth_firefox_driver,
            'authenticated_safari': self.get_auth_safari_driver,
            'authenticated_local_ga_chrome': self.get_authenticated_local_ga_chrome,
            'authenticated_remote_ga_chrome': self.get_authenticated_remote_ga_chrome,
            'headless_authenticated_chrome': self.get_headless_authenticated_chrome_driver,
            'headless_authenticated_firefox': self.get_headless_auth_firefox_driver,
            'authenticated_local_html_validator': self.get_authenticated_local_html_validator,
            'remote_authenticated_chrome': self.get_remote_authenticated_chrome_driver,
            'authenticated_remote_html_validator': self.get_authenticated_remote_html_validator,
            'remote_authenticated_firefox': self.get_remote_authenticated_firefox_driver,
        }
        return self.drivers


    def get_browser_driver(self):
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(DRIVER)()


    def get_driver_by_name(self, name):
        print('Getting Custom Driver: %s' % name)
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(name)()
