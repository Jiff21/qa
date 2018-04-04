import requests
import sys
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then, step
from qa.settings import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH, PAGES_DICT

@step('I am on "{page_name}"')
def get(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = BASE_URL + PAGES_DICT[context.page_name]
    print('On this url %s' % context.current_url)
    context.driver.get(context.current_url)

@step('I check logs')
def check_console_logs(context):
    context.current_url = BASE_URL + '/'
    context.driver.get(context.current_url)
    context.captured_logs = ['']
    for entry in context.driver.get_log('browser'):
        if 'https://www.google-analytics.com/analytics_debug.js' in entry['message']:
            context.captured_logs.append(entry['message'])

@step('I close new tab')
def check_console_logs(context):
    context.driver.switch_to_window(context.driver.window_handles[+1])
    context.driver.close()
    context.driver.switch_to_window(context.driver.window_handles[-1])

@step('I should see "{ga_name}" with a value of "{ga_value}"')
def assert_no_errors_in_logs(context, ga_name, ga_value):
    context.text_found = False
    context.ga_search = CommonFunctions()
    for entry in context.captured_logs:
        if context.ga_search.find_ga_by_terms(entry, ga_name, ga_value):
            print ('Found: %s' % entry)
            context.text_found = True
    try:
        assert context.text_found is True, \
            "Didn\'t get expected for %s. Instead:\n%s" % (
                entry,
                str(context.ga_search.find_ga_by_terms(entry, ga_name, ga_value))
            )
    except AssertionError:
        print ('Didn\'t find expected ga tag, found:\n')
        for message in context.captured_logs:
            print (str(message))
        raise


class CommonFunctions(object):

    def get_response_code(self, api_url, headers):
        self.resp = requests.get(api_url, headers=headers)
        return self.resp.status_code

    def find_ga_by_terms(self, message, ga_name, ga_value):
        my_regex = re.escape(ga_name) + r".*." + re.escape(ga_value)
        if re.search(my_regex, message, re.IGNORECASE):
            return True

    def find_ga_by_name(self, message, ga_name):
        my_regex = re.escape(ga_name) + r".*."
        if re.search(my_regex, message, re.IGNORECASE):
            return True

    def everything_after(self, log_line):
        catch_value = r'(?<=.       \(&..\)   )(.*)'
        found = re.search(catch_value, log_line, re.IGNORECASE)
        return found
