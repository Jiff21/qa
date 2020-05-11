import csv
import os
from behave import given, when, then, step
from qa.settings import HOST_URL, PAGES_DICT, QA_FOLDER_PATH
from qa.settings import log


LOCUST_RESULTS_FILE = '%s/performance/results/_stats.csv' % QA_FOLDER_PATH

def get_page_value(passed_array, uri_name, value_to_find):
    for row in passed_array:
        if row['Name'] == uri_name:
            return row[value_to_find]


@step('request results file exists')
def step_impl(context):
    try:
        context.csv_dict = csv.DictReader(open(LOCUST_RESULTS_FILE))
    except:
        print('Error getting results file')
        raise

@step('we get "{column_name}" for the page "{page_name}"')
def step_impl(context, column_name, page_name):
    log.debug(
        'we get %s for the page %s' % (
            column_name,
            page_name
        )
    )
    if page_name.lower() == 'index':
        # Google Currently adding traling spaces
        locust_page_name = '/'
    else:
        locust_page_name =  PAGES_DICT[page_name]
    context.current_value = get_page_value(
        context.csv_dict,
        locust_page_name,
        column_name
    )
    assert context.current_value is not None, \
        'An error occured locating %s for %s' % (
            column_name,
            locust_page_name
    )


@step('it should be lower than or equal to "{number:d}"')
def step_impl(context, number):
    assert int(context.current_value) <= number, \
        'Expected a value under %d, instead got %s' % (
            number,
            context.current_value,
        )
