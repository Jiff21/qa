import csv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.common.keys import Keys
from behave import given, when, then, step
from qa.settings import BASE_URL


def get_page_value(passed_array, uri_name, value_to_find):
    for row in passed_array:
        if row['Name'] == uri_name:
            return row[value_to_find]

@step('request results file exists')
def step_impl(context):
    try:
        context.csv_dict = reader = csv.DictReader(open('qa/performance/results/_requests.csv'))
    except:
        assert 1 == 2, 'Error getting results file'

@step('we get "{column_name}" for the page "{uri}"')
def step_impl(context, column_name, uri):
    context.driver.current_value = get_page_value(context.csv_dict, uri, column_name)

@step('it should be lower than or equal to "{number:d}"')
def step_impl(context, number):
    assert int(context.driver.current_value) <= number, \
        'Expected a value under %d, insted got %d' % (
            number,
            context.driver.current_value,
        )
