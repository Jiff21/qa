'''
  Scenario: The Homepage fires an event when it loads
    When I check logs
    Then this should happen when page loads.

'''
import time
from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH


@when('I check logs')
def check_console_logs(context):
    context.current_url = BASE_URL + '/'
    context.driver.get(context.current_url)
    context.captured_logs = ['']
    for entry in context.driver.get_log('browser'):
        context.captured_logs.append(entry)


@then('this should happen when page loads.')
def assert_no_errors_in_logs(context):
    try:
        for entry in context.captured_logs:
            print (entry)
            time.sleep(20)
            assert len(entry) == 2
            # assert len(context.verificationErrors) == 0
    except AssertionError:
        for message in context.captured_logs:
            print (str(message))
        raise
