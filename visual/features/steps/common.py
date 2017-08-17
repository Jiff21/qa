from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC
from behave import given, when, then, step
from applitools.common import StitchMode
from applitools.eyes import Eyes
from applitools.eyes import MatchLevel
from applitools.geometry import Region


# SIZE MAPS
WIDTH_DICT = {
    'tablet': 800,
    'mobile': 600
}
HEIGHT_DICT = {
    'tablet': 600,
    'mobile': 400
}


@given('I start "{test_name}" of "{app_name}" at "{size}"')
def start_eyes(context, size, test_name, app_name):
    context.eyes.open(
        driver=context.driver,
        app_name=app_name,
        test_name=test_name,
        viewport_size={'width': WIDTH_DICT[size], 'height': HEIGHT_DICT[size]}
    )
    context.eyes.match_level = MatchLevel.LAYOUT2


@given('I start "{test_name}" of "{app_name}')
def start_no_size(context, test_name, app_name):
    context.eyes.open(
        driver=context.driver,
        app_name=app_name,
        test_name=test_name,
    )


@given('I force fullscreen mode')
def full_screen(context):
    context.eyes.force_full_page_screenshot = True
    context.eyes.stitch_mode = StitchMode.CSS


@step('I am on "{uri}"')
def get_url(context, uri):
    url = BASE_URL + uri
    context.driver.get(url)


@step('The "{message}" should look as expected')
def check_expect_given(context, message):
    context.eyes.check_window(message)


@then('we close eyes')
def step_then_should_transform_into(context):
    context.eyes.close()
    context.eyes.abort_if_not_closed()
