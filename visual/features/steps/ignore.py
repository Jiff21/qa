'''
    Given I am on "/behave/"
      And I start "Home to other pages test" of "python hosted" at "tablet"
    When only the body of the "home page body" should look as expected
      And I am on "/behave/api.html"
    Then the "API Page" should look as expected, without the headerlink
      And I ignore the "Region Selector" by dimensions
      and we close eyes

'''
from applitools.target import Target, IgnoreRegionBySelector, FloatingRegion, FloatingBounds
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from behave import given, when, then
from qa.settings import BASE_URL, DRIVER, SELENIUM, SL_DC
from applitools.geometry import Region
from applitools.common import StitchMode

# Locator Map
BODY_LOCATOR = (By.CSS_SELECTOR, 'div.body')
HEADER_LINK = (By.CSS_SELECTOR, '#behave-api-reference > h1 > a')


@when('only the body of the "{message}" should look as expected')
def check_expect_given(context, message):
    context.body = context.driver.find_element(*BODY_LOCATOR)
    context.eyes.check_region_by_element(
        context.body, message, target=Target())


@then('the "{message}" should look as expected, without the headerlink')
def check_expect_given(context, message):
    context.eyes.check_window(message, target=Target().ignore(
        IgnoreRegionBySelector(*HEADER_LINK))
    )


@then('I ignore the "{message}" by dimensions')
def check_expect_given(context, message):
    context.eyes.check_window(message, target=Target().ignore(
        Region(1185, 30, 1158, 76)
    )
    )
