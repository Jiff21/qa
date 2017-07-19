'''
Feature: The about page's style doesn't accidentally change

  @browser
  Scenario: I go to the about page on a tablet it should look as expected
    Given I am on "/"
      And I start "Home to other pages test" of "example.com" at "tablet"
    When the "Home Page" should look as expected
      And I click the sf office image
      And locate the header
    Then the "Contact Page" should look as expected
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
SF_OFFICE = (By.CSS_SELECTOR, 'a.office.sfo')
CONTACT_HEADER = (By.CSS_SELECTOR, 'p.strapline')


@when('I click the sf office image')
def click_a_button(context):
    sf_office_icon = context.driver.find_element(*SF_OFFICE)
    time.sleep(10)
    sf_office_icon.click()


@when('locate the header')
def step_then_should_transform_into(context):
    header = context.driver.find_element(*CONTACT_HEADER)
    actions = ActionChains(context.driver)
    actions.move_to_element(header)
    actions.perform()
