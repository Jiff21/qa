'''
Feature: Example.com should have a head

  @browser
  Scenario: This is a scenario name
    Given I am on "https://example.com"
    Then the header should be exactly "Example Domain"
'''
import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Locator Map
HEADER_PATH = (By.CSS_SELECTOR, 'section.section.blog > h2.section-title')
SEARCH_FIELD_SELECTOR = (By.XPATH, '//input[@aria-label="Search"]')
SUBMIT_BUTTON = (By.XPATH, '//center/input[@name="btnK"]')
RESULTS_WAIT = (By.ID, 'cnt')
RESULTS_ASSERTION = (By.XPATH, '//*[@id="rso"]//a')


@when('I type in "{thing}"')
def step_impl(context, thing):
    el = context.driver.find_element(*SEARCH_FIELD_SELECTOR)
    el.send_keys(thing)
    el.send_keys(Keys.ENTER)


@then('the results should contain "{word}"')
def step_impl(context, word):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located(RESULTS_WAIT))
    el = context.driver.find_element(*RESULTS_ASSERTION)
    assert word in el.text, "Did not get expected text, instead:\n%s" % (
        el.text
    )


@then('the header should be exactly "{words}"')
def step_impl(context, words):
    el = context.driver.find_element(*HEADER_PATH)
    assert el.text == words

@step('I click the start test button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#action-start-test')))
    el = context.driver.find_element(By.CSS_SELECTOR, '#action-start-test')
    el.click()
    time.sleep(40)
