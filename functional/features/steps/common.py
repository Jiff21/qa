import time
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from qa.settings import BASE_URL, PAGES_DICT
from workarounds import scroll_to_webelement
from custom_exceptions import loop_thru_messages
from hover_state import *

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

@step('I am on "{page_name}"')
def get(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = BASE_URL + PAGES_DICT[context.page_name]
    print('On this url %s' % context.current_url)
    context.driver.get(context.current_url)

@step('I check the console logs')
def step_impl(context):
    context.console_errors = []
    for entry in context.driver.get_log('browser'):
        try:
            assert "SEVERE" not in entry['level']
        except AssertionError:
            context.console_errors.append(
                "On Page: %s. Expeced no errors in log instead got:\n%s" % (
                    context.current_url,
                    str(entry)
                )
            )

@step('there should be no severe console log errors')
def step_impl(context):
    assert len(context.console_errors) == 0, loop_thru_messages(context.console_errors)
    # try:
    #     assert len(context.console_errors) == 0
    # except AssertionError:
    #     raise LoopThruMessagesException(context.console_errors)


@step('I throttle network speed to "{down:f}" MB/s down, "{up:f}" MB/s up, with "{latency:f}" ms latency')
def step_impl(context, down, up, latency):
    print('Toggling speeds with ' + str(down) + ' down and ' + str(up) + ' up')
    conversion = 18000
    print(down * conversion)
    context.driver.set_network_conditions(
        offline=False,
        latency=latency,  # additional latency (ms)
        download_throughput=down * conversion,  # maximal throughput
        upload_throughput=up * (conversion * 2)
        # download_throughput=down * 8000,  # maximal throughput
        # upload_throughput=up * 8000
    )

@step('I look for html validator messages')
def step_impl(context):
    context.html_validation_errors = []
    time.sleep(2)
    for entry in context.driver.get_log('browser'):
        if 'console-api' in entry['message']:
            if 'Document is valid' not in entry['message']:
                context.html_validation_errors.append(
                    'On Page: %s. Expected no html validator messages in log ' \
                    'instead got:\n%s' % (
                        context.current_url,
                        str(entry)
                    )
                )

@step('it should not have any validation errors')
def step_impl(context):
    assert len(context.html_validation_errors) == 0, loop_thru_messages(context.html_validation_errors)
    # try:
    #     assert len(context.html_validation_errors) == 0
    # except AssertionError:
    #     raise LoopThruMessagesException(context.html_validation_errors)
