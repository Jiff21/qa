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
from qa.functionality.features.steps.common import easy_wait
import time


# Locator Map
SEARCH_FIELD_SELECTOR = (By.XPATH, '//input[@aria-label="Search"]')
SUBMIT_BUTTON = (By.XPATH, '//center/input[@name="btnK"]')
RESULTS_WAIT = (By.ID, 'cnt')
RESULTS_ASSERTION = (By.XPATH, '//*[@id="rso"]//a')


@when('I type in "{thing}"')
def send_keys_to_field(context, thing):
    el = context.driver.find_element(*SEARCH_FIELD_SELECTOR)
    el.send_keys(thing)
    el.send_keys(Keys.ENTER)


@then('the results should contain "{word}"')
def step_then_should_transform_into(context, word):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located(RESULTS_WAIT))
    el = context.driver.find_element(*RESULTS_ASSERTION)
    assert_that(el.text, contains_string(word))
