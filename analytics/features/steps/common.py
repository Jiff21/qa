import requests
import sys
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH


@given('I am on "{uri}"')
def get(context, uri):
    current_url = BASE_URL + uri
    context.driver.get(current_url)


class CommonFunctions(object):

    def get_response_code(self, api_url, headers):
        self.resp = requests.get(api_url, headers=headers)
        return self.resp.status_code

    def find_ga_by_terms(self, message, ga_name, ga_value):
        my_regex = re.escape(ga_name) + r".*." + re.escape(ga_value)
        if re.search(my_regex, message, re.IGNORECASE):
            return True
