'''
Feature: The about page's style doesn't accidentally change

  @browser
  Scenario: I go to the about page on a tablet it should look as expected
    Given I start eyes at "tablet"
    When I type in "hello world!"
      and click a certain button
    Then it should look a certain way with the message "Click!"
        and we close eyes
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC
from qa.e2e.features.browser import Browser
import time


# Locator Map
SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button')


@when('and click a certain button')
def click_a_button(context):
    context.driver.find_element(*SUBMIT_BUTTON)


@then('it should look a certain way with the message "{message}"')
def step_then_should_transform_into(context, message):
    context.eyes.check_window(message)
