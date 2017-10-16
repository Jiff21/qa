import csv
import os
from behave import given, when, then, step
from qa.settings import BASE_URL


def get_page_value(passed_array, uri_name, value_to_find):
    for row in passed_array:
        if row['Name'] == uri_name:
            return row[value_to_find]


@step('request results file exists')
def step_impl(context):
    try:
        context.csv_dict = csv.DictReader(open('qa/performance/results/_requests.csv'))
    except:
        print('Error getting results file')
        raise

@step('we get "{column_name}" for the page "{uri}"')
def step_impl(context, column_name, uri):
    context.current_value = get_page_value(context.csv_dict, uri, column_name)
    print(context.current_value)
    assert context.current_value is not None, 'An error occured locating %s for %s' % (column_name, uri)

@step('it should be lower than or equal to "{number:d}"')
def step_impl(context, number):
    assert int(context.current_value) <= number, \
        'Expected a value under %d, insted got %s' % (
            number,
            context.current_value,
        )
