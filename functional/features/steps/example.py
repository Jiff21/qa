'''
Feature: Example.com should have a head

  @browser
  Scenario: This is a scenario name
    Given I am on "https://example.com"
    Then the header should be exactly "Example Domain"
'''
from behave import given, when, then
from chai import Chai
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Locator Map
HEADER_PATH = (By.CSS_SELECTOR, 'section.section.blog > h2.section-title')


@then('the header should be exactly "{words}"')
def step_impl(context, words):
    el = context.driver.find_element(*HEADER_PATH)
    assert el.text == words
