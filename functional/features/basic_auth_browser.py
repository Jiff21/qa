import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa.settings import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_BROWSER_POSITION
from qa.settings import HOST_URL, DRIVER, SELENIUM, CLIENT_ID
from qa.settings import log
from qa.settings import SL_DC, QA_FOLDER_PATH
from qa.utilities.mod_header.custom_headers import create_modheaders_plugin
from qa.utilities.oauth.basic_auth_headers import get_encoded_auth_token


def dict_from_string(current_dict, string):
    for item in string.split(','):
        key, value = item.split(':')
        current_dict[key.strip(' \"}{:')] = value.strip(' \"}{:')
    return current_dict

def debug_chrome_options(opt):
    log.debug('These the chrome options')
    for item in opt.arguments:
        log.debug(str(item))

def validity_path():
    if 'linux' in sys.platform:
        validity_path = '/usr/bin/Validity.crx'
    else:
        validity_path = 'qa/utilities/html_validator/Validity.crx'
    log.debug('Validity path is %s' % validity_path)
    return validity_path


def set_defaults(browser_obj):
    browser_obj.set_window_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)
    # Keep position 2nd or Safari will reposition on set_window_size
    browser_obj.set_window_position(
        DEFAULT_BROWSER_POSITION['x'],
        DEFAULT_BROWSER_POSITION['y']
    )

class Browser(object):

    def __init__(self, **kwargs):
        log.info('Setting up Browsermob Browser List')
        self.normal_browser = NormalBrowser()

    def generic_chrome_dc(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.desired_capabilities['acceptInsecureCerts'] = True
        return self.desired_capabilities


    def get_authenticated_chrome_driver(self):
        self.auth_token = get_encoded_auth_token()
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.auth_token
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

    def get_headless_authenticated_chrome_driver(self):
        self.auth_token = get_encoded_auth_token()
        self.custom_modified_headers = create_modheaders_plugin(
            remove_headers=[],
            add_or_modify_headers={
                "Authorization": self.auth_token
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


    def return_driver_dict(self):
        self.drivers = {
            'authenticated_chrome': self.get_authenticated_chrome_driver,
            'chrome': self.normal_browser.get_chrome_driver,
            'custom_device': self.normal_browser.get_custom_emulation,
            'ga_chrome': self.normal_browser.get_local_ga_chrome,
            'local_html_validator': self.normal_browser.get_local_html_validator,
            'firefox': self.normal_browser.get_firefox_driver,
            'galaxy_s8': self.normal_browser.get_galaxy_s8_emulation,
            'headless_authenticated_chrome': self.get_headless_authenticated_chrome_driver,
            'headless_chrome': self.normal_browser.get_headless_chrome,
            'headless_firefox': self.normal_browser.get_headless_firefox_driver,
            'nexus_5x': self.normal_browser.get_nexus_5x_emulation,
            'iphone_7': self.normal_browser.get_iphone_7_emulation,
            'safari': self.normal_browser.get_safari_driver,
            'saucelabs': self.normal_browser.get_sauce_driver,
            'remote_ga_chrome': self.normal_browser.get_remote_ga_chrome,
            'remote_html_validator': self.normal_browser.get_remote_html_validator,
            'remote_firefox': self.normal_browser.get_remote_firefox_driver,
            'remote_safari': self.normal_browser.get_remote_safari_driver,
            'remote_headless_chrome': self.normal_browser.get_remote_headless_chrome
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
            log.info('Unrecognized Driver from Command Line Arguement')
        else:
            return drivers.get(name)()
