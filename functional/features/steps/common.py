from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from qa.settings import BASE_URL, PAGES_DICT


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
    context.verificationErrors = []
    for entry in context.driver.get_log('browser'):
        try:
            assert "SEVERE" not in entry['level']
        except AssertionError:
            context.verificationErrors.append(
                "On Page: %s. Expeced no errors in log instead got:\n%s" % (
                    context.current_url,
                    str(entry)
                )
            )

@step('there should be no severe console log errors')
def step_impl(context):
    try:
        assert len(context.verificationErrors) == 0
    except AssertionError:
        for message in context.verificationErrors:
            print (str(message))
        raise

@step('I throttle network speed to "{down:f}" MB/s down, "{up:f}" MB/s up, with "{latency:f}" ms latency')
def step_impl(context, down, up, latency):
    print('Toggling speeds with ' + str(down) + ' down and ' + str(up) + ' up')
    driver.set_network_conditions(
        offline=False,
        latency=latency,  # additional latency (ms)
        download_throughput=down * 8000,  # maximal throughput
        upload_throughput=up * 8000
    )
