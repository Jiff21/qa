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



class Browser(object):


    def __init__(self, bearer_header=None, proxy=None, server=None, passthrough=None, **kwargs):
        print ('Setting up Browsermob Browser List')
        self.normal_browser = NormalBrowser()
        self.bearer_header = bearer_header
        self.proxy = proxy
        self.server = server
        self.passthrough = passthrough


    def setup_browsermob_proxy(self, proxy_host, proxy_port, no_proxy):
        proxy_address = '{}:{}'.format(proxy_host, proxy_port)
        self.chrome_options.add_argument('--proxy-server=%s' % proxy_address)
        no_proxy_string = ';'.join(no_proxy)
        self.chrome_options.add_argument('--proxy-bypass-list=%s' % no_proxy_string)
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api"
        )
        return self.chrome_options


    def generic_chrome_dc(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.desired_capabilities['acceptInsecureCerts'] = True
        return self.desired_capabilities


    def setup_firefox_proxy(self, proxy_host, proxy_port, no_proxy):
        # self.desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        proxy_address = '{}:{}'.format(proxy_host, proxy_port)
        self.desired_capabilities['proxy'] = {
            'proxyType': "MANUAL",
            'httpProxy': proxy_address,
            'sslProxy': proxy_address,
            'noProxy': no_proxy
        }
        self.desired_capabilities['acceptInsecureCerts'] = True
        self.desired_capabilities['javascriptEnabled'] = True
        return self.desired_capabilities


    def get_authenticated_chrome_driver(self):
        self.chrome_options = self.normal_browser.mandatory_chrome_options()
        self.chrome_options = self.setup_browsermob_proxy(self.server.host, self.proxy.port, self.passthrough)
        self.desired_capabilities = self.generic_chrome_dc()
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        # Get a WebDriver instance
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )
        self.normal_browser.set_defaults(self.browser)
        return self.browser


    def get_remote_authenticated_chrome_driver(self):
        self.chrome_options = self.normal_browser.mandatory_chrome_options()
        self.chrome_options = self.setup_browsermob_proxy(self.server.host, self.proxy.port, self.passthrough)
        self.desired_capabilities = self.generic_chrome_dc()
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        # Get a WebDriver instance
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.normal_browser.set_defaults(self.browser)
        return self.browser


    def get_headless_authenticated_chrome_driver(self):
        self.chrome_options = self.normal_browser.mandatory_chrome_options()
        self.chrome_options = self.setup_browsermob_proxy(self.server.host, self.proxy.port, self.passthrough)
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        # Get a WebDriver instance
        self.browser = webdriver.Chrome(
            executable_path='qa/env/bin/chromedriver',
            options=self.chrome_options,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.normal_browser.set_defaults(self.browser)
        return self.browser


    def get_cloud_build_authenticated_chrome_driver(self):
        self.chrome_options = self.normal_browser.mandatory_chrome_options()
        self.chrome_options = self.setup_browsermob_proxy(self.server.host, self.proxy.port, self.passthrough)
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        # My Alipine install
        self.chrome_options.binary_location = '/usr/bin/chromium-browser'
        # # My Debianinstall
        # self.chrome_options.binary_location = '/usr/bin/google-chrome'
        self.desired_capabilities = self.generic_chrome_dc()
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Chrome(
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.normal_browser.set_defaults(self.browser)
        return self.browser


    def get_authenticated_local_ga_chrome(self):
        self.chrome_options = self.normal_browser.mandatory_chrome_options()
        self.chrome_options = self.setup_browsermob_proxy(self.server.host, self.proxy.port, self.passthrough)
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options.add_extension(
            '%senv/bin/ga_tracker.crx' % QA_FOLDER_PATH
        )
        # Get a WebDriver instance
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.driver


    def get_authenticated_remote_ga_chrome(self):
        self.chrome_options = self.normal_browser.mandatory_chrome_options()
        self.chrome_options = self.setup_browsermob_proxy(self.server.host, self.proxy.port, self.passthrough)
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
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
        self.chrome_options = self.setup_browsermob_proxy(self.server.host, self.proxy.port, self.passthrough)
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options.add_extension(
            '%sutilities/html_validator/Validity.crx' % QA_FOLDER_PATH
        )
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.browser


    def get_authenticated_remote_html_validator(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options = self.setup_browsermob_proxy(self.server.host, self.proxy.port, self.passthrough)
        self.desired_capabilities = self.generic_chrome_dc()
        # self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
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
        self.desired_capabilities = self.normal_browser.setup_firefox_dc()
        self.desired_capabilities = self.setup_firefox_proxy(self.server.host, self.proxy.port, self.passthrough)

        # get a driver on the proxy
        self.browser = webdriver.Firefox(capabilities=self.desired_capabilities)

        # Desktop size
        self.normal_browser.set_defaults(self.browser)
        return self.browser



    def get_headless_auth_firefox_driver(self):
        self.desired_capabilities = self.normal_browser.setup_firefox_dc()
        self.desired_capabilities = self.setup_firefox_proxy(self.server.host, self.proxy.port, self.passthrough)
        options = FirefoxOptions()
        options.headless = True
        # Add Bearer headers to browsermob proxy
        profile  = webdriver.FirefoxProfile()
        profile.set_proxy(self.proxy.selenium_proxy())
        # get a driver on the proxy
        self.browser = webdriver.Firefox(
            capabilities=self.desired_capabilities,
            firefox_profile=profile,
            options=options
        )
        # Desktop size
        self.normal_browser.set_defaults(self.browser)
        return self.browser


    def get_remote_authenticated_firefox_driver(self):
        self.desired_capabilities = self.normal_browser.setup_firefox_dc()
        self.desired_capabilities = self.setup_firefox_proxy(self.server.host, self.proxy.port, self.passthrough)
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
        # self.normal_browser.set_defaults(browser)
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
            'remote_headless_chrome': self.normal_browser.get_remote_headless_chrome,
            'authenticated_chrome': self.get_authenticated_chrome_driver,
            'authenticated_firefox': self.get_auth_firefox_driver,
            'authenticated_safari': self.get_auth_safari_driver,
            'authenticated_local_ga_chrome': self.get_authenticated_local_ga_chrome,
            'authenticated_remote_ga_chrome': self.get_authenticated_remote_ga_chrome,
            'authenticated_headless_gcp_chrome' : self.get_cloud_build_authenticated_chrome_driver,
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
