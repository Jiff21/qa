import requests
import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.settings import BASE_URL, PAGES_DICT

# Locator Map
ABOUT_NAV_ITEM = (By.CSS_SELECTOR, 'nav.top-nav a[title*="About"]')
SEARCH_FIELD_SELECTOR = (By.XPATH, '//input[@aria-label="Search"]')
SUBMIT_BUTTON = (By.XPATH, '//center/input[@name="btnK"]')
RESULTS_WAIT = (By.ID, 'cnt')
RESULTS_ASSERTION = (By.XPATH, '//*[@id="rso"]//a')


@step('I type in "{thing}"')
def step_impl(context, thing):
    el = context.driver.find_element(*SEARCH_FIELD_SELECTOR)
    el.send_keys(thing)
    el.send_keys(Keys.ENTER)


@step('the results should contain "{word}"')
def step_impl(context, word):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located(RESULTS_WAIT))
    el = context.driver.find_element(*RESULTS_ASSERTION)
    assert word in el.text, "Did not get expected text, instead:\n%s" % (
        el.text
    )


@step('the about nav item should be undelined')
def step_impl(context):
    # try:
    el = context.driver.find_element(*ABOUT_NAV_ITEM)
    underline = el.value_of_css_property('border-bottom-color')
    assert underline == 'rgb(26, 115, 232)', 'Did not get expected Underline, instead %s' % (
        underline
    )
    # except:
    #     raise ValueError('Could not locate About Underline')

@step('I hit the robots.txt url')
def step_impl(context):
    context.response = requests.get(BASE_URL + '/robots.txt')

@step('it should have a "{code:d}" status code')
def step_impl(context, code):
    assert context.response.status_code == code, \
    'Did not get %s response, instead %i' % (
        code,
        context.response.status_code
    )

@step('it should contain User-agent: *')
def step_impl(context):
    assert 'User-agent: *' in context.response.text, \
    'Did not find User-agent: * in response.'
