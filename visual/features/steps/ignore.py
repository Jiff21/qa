'''
    Given I am on "/behave/"
      And I start "Home to other pages test" of "python hosted" at "tablet"
    When the "home page" should look as expected, without the body
      And I am on "/behave/api.html"
    Then the "API Page" should look as expected, without the body
      and we close eyes

'''
from applitools.target import Target, IgnoreRegionBySelector, FloatingRegion, FloatingBounds
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from behave import given, when, then
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC
from qa.e2e.features.browser import Browser

# Locator Map
BODY_LOCATOR = (By.CSS_SELECTOR, 'div.body')


@then('the "{message}" should look as expected, without the body')
def check_expect_given(context, message):
    context.eyes.check_window(message, target=Target().ignore(
        IgnoreRegionBySelector(*BODY_LOCATOR))
    )


@when('the "{message}" should look as expected, without the body')
def check_expect_given(context, message):
    context.eyes.check_window(message, target=Target().ignore(
        IgnoreRegionBySelector(*BODY_LOCATOR))
    )
