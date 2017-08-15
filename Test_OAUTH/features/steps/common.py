import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from behave import given, when, then, step
from qa.environment_variables import BASE_URL


class easy_wait():

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, locator, type="By.CSS_SELECTOR"):
        element = None
        try:
            wait = WebDriverWait(
                self.driver,
                10,
                poll_frequency=1,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException
                ]
            )
            element = wait.until(EC.element_to_be_clickable(
                self.driver.find_element(type, locator)
            ))
        except:
            print('Could not find element with %s using %s' % (
                locator,
                type
            ))
        return element


@step('I am on "{uri}"')
def get(context, uri):
    context.current_url = ''
    if uri.lower() == 'index':
        context.current_url = BASE_URL
    else:
        context.current_url = BASE_URL + uri
    context.driver.get(context.current_url)
