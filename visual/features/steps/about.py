'''
Feature: Behave's Predefined Data Types in parse page

  @browser
  Scenario:
    Given I am on "/behave/parse_builtin_types.html"
      And I start "Home to other pages test" of "example.com" at "tablet"
    When the "Data Types Page" should look as expected
      And I type in "Dogs"
      And click Go
      And wait for page to load
    Then I see the no results header
      and the "No Results Page" should look as expected
      and we close eyes

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from behave import given, when, then
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC
from qa.e2e.features.browser import Browser
import time

# Locator Map
SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, 'form.search > input[name="q"]')
GO_BUTTON = (By.CSS_SELECTOR, 'form.search > input[value="Go"]')
RESULTS_WAIT = (By.CSS_SELECTOR, 'div#search-results')
NO_RESULTS_LOCATOR = (By.CSS_SELECTOR, 'div#search-results > h2')


@when('I type in "{search_term}"')
def click_a_button(context, search_term):
    search_field = context.driver.find_element(*SEARCH_FIELD_LOCATOR)
    search_field.send_keys(search_term)


@when('click Go')
def click_a_button(context):
    go_button = context.driver.find_element(*GO_BUTTON)
    go_button.click()


@when('wait for page to load')
def step_then_should_transform_into(context):
    wait = WebDriverWait(context.driver, 20)
    wait.until(EC.presence_of_element_located(RESULTS_WAIT))


@then('I see the no results header')
def step_then_should_transform_into(context):
    results_header = context.driver.find_element(*NO_RESULTS_LOCATOR)
    assert results_header.is_displayed() == True, 'Could not find results'
