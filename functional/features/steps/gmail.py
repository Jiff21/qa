'''
Feature: Login test

  @browser
  Scenario: Check Mail
    Given I am on "/"
      And I click Mail
      And I click Sign In
    When I log into google using as "Admin"
      And I wait for the page to load
    Then I am on inbox page

'''
from behave import given, when, then
from chai import Chai
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Locator Map
MAIL_LINK_LOCATOR = (By.XPATH, '//div/a[contains(text(),"Gmail")]')
SIGN_IN_LINK_LOCATOR = (By.CSS_SELECTOR, 'a.gmail-nav__nav-link__sign-in')
ACCOUNT_ICON_LOCATOR = (By.XPATH, '//a[starts-with(@title,"Google Account:")]')


@given('I click Mail')
def step_impl(context):
    el = context.driver.find_element(*MAIL_LINK_LOCATOR)
    el.click()


@given('I click Sign In')
def step_impl(context):
    el = context.driver.find_element(*SIGN_IN_LINK_LOCATOR)
    el.click()


@when('I wait for the page to load')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    print(context.driver.current_url)
    wait.until(EC.visibility_of_element_located(ACCOUNT_ICON_LOCATOR))


@then('I am on inbox page')
def step_impl(context):
    current_url = context.driver.current_url
    print(current_url)
    assert 'https://mail.google.com' in current_url, \
        'Did not end up in Inbox, instead:\n%s' % current_url
