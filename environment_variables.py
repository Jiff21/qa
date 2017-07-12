import os

BASE_URL = os.getenv('BASE_URL', 'http://localhost:3000')
DRIVER = os.getenv('DRIVER', 'headless_chrome')
DRIVER = DRIVER.lower().replace(' ', '_').replace('-', '_')
SELENIUM = os.getenv('SELENIUM', 'http://localhost:4444/wd/hub')
SL_DC = os.getenv(
    'SL_DC',
    '{"platform": "Mac OS X 10.9", "browserName": "chrome", "version": "31"}'
)
PAGES_LIST = ['/about', 'contact']
QA_FOLDER_PATH = ''


def dict_from_string(current_dict, string):
    for item in string.split(','):
        key, value = item.split(':')
        current_dict[key.strip(' \"}{:')] = value.strip(' \"}{:')
    return current_dict


def set_defaults(browser_obj):
    browser_obj.set_window_position(0, 0)
    browser_obj.set_window_size(1366, 768)


def get_chrome_driver():
    desired_capabilities = webdriver.DesiredCapabilities.CHROME
    desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "--disable-plugins --disable-instant-extended-api")

    desired_capabilities.update(chrome_options.to_capabilities())

    browser = webdriver.Chrome(
        executable_path='chromedriver',
        desired_capabilities=desired_capabilities
    )

    # Desktop size
    set_defaults(browser)
    return browser


def get_headless_chrome():
    desired_capabilities = webdriver.DesiredCapabilities.CHROME
    desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "--disable-plugins --disable-instant-extended-api \
        --headless")

    desired_capabilities.update(chrome_options.to_capabilities())

    browser = webdriver.Remote(
        command_executor=SELENIUM,
        desired_capabilities=desired_capabilities
    )

    # Desktop size
    set_defaults(browser)
    return browser


def get_firefox_driver():

    browser = webdriver.Firefox()

    # Desktop size
    set_defaults(browser)
    return browser


def get_remote_firefox_driver():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
    desired_capabilities['acceptInsecureCerts'] = True
    desired_capabilities['javascriptEnabled'] = True

    browser = webdriver.Remote(
        command_executor=SELENIUM,
        desired_capabilities=desired_capabilities
    )


def get_safari_driver():

    browser = webdriver.Safari()
    # SETTING WIDTH HERE BREAKS SAFARI
    # set_defaults(browser)
    return browser


def get_remote_safari_driver():
    # For use with selenium hub
    desired_capabilities = webdriver.DesiredCapabilities.SAFARI
    desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
    desired_capabilities['maxInstances'] = 1
    desired_capabilities['maxSession'] = 1
    desired_capabilities['acceptSslCerts'] = True
    # desired_capabilities['useTechnologyPreview'] = True
    desired_capabilities['useCleanSession'] = True

    browser = webdriver.Remote(
        command_executor=SELENIUM,
        desired_capabilities=desired_capabilities
    )

    return browser


def get_sauce_driver():
    # For use with selenium hub
    desired_capabilities = {}
    desired_capabilities = dict_from_string(desired_capabilities, SL_DC)
    browser = webdriver.Remote(
        command_executor=SELENIUM,
        desired_capabilities=desired_capabilities
    )
    return browser


DRIVERS = {
    'chrome': get_chrome_driver,
    'firefox': get_firefox_driver,
    'remote_firefox': get_remote_firefox_driver,
    'headless_chrome': get_headless_chrome,
    'safari': get_safari_driver,
    'remote_safari': get_remote_safari_driver,
    'saucelabs': get_sauce_driver
}


def get_browser_driver():
    if DRIVER not in DRIVERS:
        print('Unrecognized Driver from Command Line Arguement')
    else:
        return DRIVERS.get(DRIVER)()
