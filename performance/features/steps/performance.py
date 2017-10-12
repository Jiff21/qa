'''
Feature: Website meets our performance standards

  Scenario: The index page has an average response under 50
    Given request results file exists
    When we get "Average response time" for the page "/"
    Then it should be lower than or equal to "50"

'''
from behave import given, when, then
import time

@then('the header should be exactly "{words}"')
def find_header(context, words):
    el = context.driver.find_element(*HEADER_PATH)
    assert_that(el.text, equal_to(words))
