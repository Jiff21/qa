'''
Feature: Website meets our performance standards

  Scenario: The index page has an average response under 50
    Given request results file exists
    When we get "Average response time" for the page "/"
    Then it should be lower than or equal to "50"

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to
import time

@then('the header should be exactly "{words}"')
def find_header(context, words):
    el = context.driver.find_element(*HEADER_PATH)
    assert_that(el.text, equal_to(words))
