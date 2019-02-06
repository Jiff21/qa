import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


def scroll_to_webelement(driver, web_element):
    '''
    actions.move_to_element will fail in firefox if you do not scroll
    the element on screen beforehand.
    '''
    if 'firefox' in driver.capabilities['browserName'] \
        or 'safari' in driver.capabilities['browserName']:
        x = web_element.location['x']
        y = web_element.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        driver.execute_script(scroll_by_coord)
        driver.execute_script(scroll_nav_out_of_way)


def safari_window_switcher(context, title):
    '''Safari has timing issues with which window is what.'''
    if 'safari' in context.driver.capabilities['browserName']:
        context.expected_title = title
        for i in range(0, len(context.driver.window_handles)):
            context.driver.switch_to_window(context.driver.window_handles[i])
            if context.driver.title == context.expected_title:
                context.handle_to_switch_to = context.driver.current_window_handle
        print(context.driver.title)
        context.driver.switch_to_window(context.handle_to_switch_to)
        assert context.driver.title == context.expected_title, \
            'Safari swindow switching issue at %s' % context.driver.current_url


def make_sure_safari_back_on_only_window(driver):
    '''
        Without this it sometimes doesn't switch to the original window.
        Oddly though the time it takes to run makes it unnecessary.
    '''
    if 'safari' in driver.capabilities['browserName']:
        if len(driver.window_handles) > 1:
            print('Waiting for only 1 tab')
            time.sleep(0.25)
            make_sure_safari_back_on_only_window(driver)
        else:
            print('Only 1 tab open!')
            driver.switch_to_window(driver.window_handles[0])


def safari_text_shim(selector_type, text_to_find, driver):
    '''Safari isn't good with XPATH text selector'''
    all_els = driver.find_elements(By.CSS_SELECTOR, selector_type)
    for el in all_els:
        if text_to_find in el.text:
            print('Found text: %s' % el.text)
            actions = ActionChains(driver)
            actions.move_to_element(el)
            actions.click()
            actions.perform()
            return


# From somebody else but works well
class LocalStorage:

    def __init__(self, driver) :
        self.driver = driver

    def __len__(self):
        return self.driver.execute_script("return window.localStorage.length;")

    def items(self) :
        return self.driver.execute_script( \
            "var ls = window.localStorage, items = {}; " \
            "for (var i = 0, k; i < ls.length; ++i) " \
            "  items[k = ls.key(i)] = ls.getItem(k); " \
            "return items; ")

    def keys() :
        return self.driver.execute_script( \
            "var ls = window.localStorage, keys = []; " \
            "for (var i = 0; i < ls.length; ++i) " \
            "  keys[i] = ls.key(i); " \
            "return keys; ")

    def get_all(self):
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def set(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def has(self, key):
        return key in self.keys()

    def remove(self, key):
        self.driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")
