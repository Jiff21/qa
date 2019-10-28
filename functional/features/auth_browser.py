import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa.settings import CLIENT_ID, DEFAULT_WIDTH, DEFAULT_HEIGHT, log
from qa.settings import HOST_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH
from qa.utilities.mod_header.custom_headers import create_modheaders_plugin
from qa.utilities.oauth.service_account_auth import make_iap_request

def dict_from_string(current_dict, string):
    for item in string.split(','):
        key, value = item.split(':')
        current_dict[key.strip(' \"}{:')] = value.strip(' \"}{:')
    return current_dict

def set_defaults(browser_obj):
    browser_obj.set_window_position(10, 30)
    browser_obj.set_window_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)


class Browser(object):


    def __init__(self, bearer_header=None, **kwargs):
        log.info('Setting up IAP only using chrome extension Browser List')
        self.normal_browser = NormalBrowser()
        self.bearer_header = bearer_header


    def get_authenticated_chrome_driver(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api")
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        set_defaults(self.browser)
        return self.browser


    def get_remote_authenticated_chrome_driver(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api")
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        set_defaults(self.browser)
        return self.browser



    def get_headless_authenticated_chrome_driver(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api --headless")
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        set_defaults(self.browser)
        return self.browser


    def get_authenticated_local_ga_chrome(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_extension(
            '%senv/bin/ga_tracker.crx' % QA_FOLDER_PATH)
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.driver


    def get_authenticated_remote_ga_chrome(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
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
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Remote(
            command_executor=SELENIUM,
            desired_capabilities=self.desired_capabilities
        )
        return self.browser


    def get__authenticated_local_html_validator(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.chrome_options.add_extension(
            '%sutilities/html_validator/Validity.crx' % QA_FOLDER_PATH)

        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.driver


    def get_authenticated_remote_html_validator(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            "--disable-plugins --disable-instant-extended-api \
            --headless")
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


    def get_authenticated_galaxy_s8_emulation(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
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
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )
        return self.browser

    def get_authenticated_nexus_5x_emulation(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
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
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )
        return self.browser


    def get_authenticated_iphone_7_emulation(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
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
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )
        return self.browser


    def get_authenticated_custom_emulation(self):
        code, self.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.bearer_header["Authorization"]
            }
        )
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
        self.chrome_options.add_extension(self.custom_modified_headers)
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            chrome_options=self.chrome_options
        )
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
            'authenticated_ga_chrome': self.get_authenticated_local_ga_chrome,
            'authenticated_remote_ga_chrome': self.authenticated_remote_ga_chrome,
            'headless_authenticated_chrome': self.get_headless_authenticated_chrome_driver,
            'authenticated_local_html_validator': self.get__authenticated_local_html_validator,
            'remote_authenticated_chrome': self.get_remote_authenticated_chrome_driver,
            'authenticated_remote_html_validator': self.get_authenticated_remote_html_validator,
            'authenticated_galaxy_s8': self.get_authenticated_galaxy_s8_emulation,
            'authenticated_iphone_7': self.get_authenticated_iphone_7_emulation,
            'authenticated_nexus_5x': self.get_authenticated_nexus_5x_emulation,
            'authenticated_saucelabs': self.get_authenticated_sauce_driver,
            'authenticated_remote_safari': self.get_authenticated_remote_safari_driver,
        }
        return self.drivers


    def get_browser_driver(self):
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(DRIVER)()


    def get_driver_by_name(self, name):
        log.info('Getting Custom Driver: %s' % name)
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            print('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(name)()
