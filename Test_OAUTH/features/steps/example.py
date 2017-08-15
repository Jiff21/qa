'''
Feature: Example.com should have a head

  @browser
  Scenario: This is a scenario name
    Given I am on "/#"
    Then the header should be exactly "Always New CMS"
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
import time


# Locator Map
HEADER_PATH = (By.CSS_SELECTOR, 'body > div.login-container > div > div > h2')


@then('the header should be exactly "{words}"')
def find_header(context, words):
    el = context.driver.find_element(*HEADER_PATH)
    assert words in el.text
