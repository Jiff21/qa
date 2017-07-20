'''
  Scenario: The Homepage fires an event when it loads
    When I check logs
    Then I should see "title" with a value of "Our Products | Google"

'''
import time
import re
from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.analytics.features.steps.common import CommonFunctions
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH


@when('I check logs')
def check_console_logs(context):
    context.current_url = BASE_URL + '/'
    context.driver.get(context.current_url)
    context.captured_logs = ['']
    for entry in context.driver.get_log('browser'):
        if 'https://www.google-analytics.com/analytics_debug.js' in entry['message']:
            context.captured_logs.append(entry['message'])


@then('I should see "{ga_name}" with a value of "{ga_value}"')
def assert_no_errors_in_logs(context, ga_name, ga_value):
    context.text_found = False
    context.ga_search = CommonFunctions()
    for entry in context.captured_logs:
        if context.ga_search.find_ga_by_terms(entry, ga_name, ga_value):
            print ('Found: %s' % entry)
            context.text_found = True
    try:
        assert context.text_found is True
    except AssertionError:
        print ('Didn\'t find expected ga tag, found:\n')
        for message in context.captured_logs:
            print (str(message))
        raise
