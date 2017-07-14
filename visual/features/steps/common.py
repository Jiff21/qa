from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC
from behave import given, when, then


# SIZE MAPS
WIDTH_DICT = {
    'tablet': 800,
    'mobile': 600
}
HEIGHT_DICT = {
    'tablet': 600,
    'mobile': 400
}


@given('I start eyes at "{size}"')
def get(context, size):
    context.eyes.open(
        driver=context.driver,
        app_name='Hello World!',
        test_name='My first Selenium Python test!',
        viewport_size={'width': WIDTH_DICT[size], 'height': HEIGHT_DICT[size]}
    )


@given('I am on "{uri}"')
def get(context, uri):
    url = BASE_URL + uri
    context.driver.get(url)


@when('I type in "{message}"')
def send_keys_to_field(context, message):
    context.eyes.check_window(message)


@then('we close eyes')
def step_then_should_transform_into(context):
    context.eyes.close()
    context.eyes.abort_if_not_closed()
