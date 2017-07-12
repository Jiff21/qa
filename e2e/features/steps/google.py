'''
Feature: Google your way to documentation

    Given I am on google.com
    When I type in "Behave Python"
      and I hit the search button
    Then the results should contain "Behave"
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to
import time


# Locator Map
SEARCH_FIELD_SELECTOR = (By.XPATH, '//input[@title="Search"]')
SUBMIT_BUTTON = (By.XPATH, '//center/input[@name="btnK"]')
RESULTS_WAIT = (By.ID, 'resultStats')
RESULTS_ASSERTION = (By.XPATH, '//*[@id="rso"]//a')


@given('I am on "{url}"')
def get(context, url):
    context.browser.get(url)


@when('I type in "{thing}"')
def send_keys_to_field(context, thing):
    el = context.browser.find_element(*SEARCH_FIELD_SELECTOR)
    el.send_keys(thing)
    el.send_keys(Keys.ENTER)


@then('the results should contain "{word}"')
def step_then_should_transform_into(context, word):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located(RESULTS_WAIT))
    el = context.browser.find_element(*RESULTS_ASSERTION)
    assert_that(el.text, contains_string(word))
