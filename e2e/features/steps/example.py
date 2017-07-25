'''
Feature: Example.com should have a head

  @browser
  Scenario: This is a scenario name
    Given I am on "https://example.com"
    Then the header should be exactly "Example Domain"
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to
import time


# Locator Map
HEADER_PATH = (By.CSS_SELECTOR, 'section.section.blog > h2.section-title')


@then('the header should be exactly "{words}"')
def find_header(context, words):
    el = context.driver.find_element(*HEADER_PATH)
    assert_that(el.text, equal_to(words))
