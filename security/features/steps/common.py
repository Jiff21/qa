import os
import json
import re
import sys
from behave import when, then, given, step
from qa.settings import BASE_URL, QA_FOLDER_PATH
from qa.functional.features.steps.custom_exceptions import loop_thru_messages


results_file = '%ssecurity/results.json' % QA_FOLDER_PATH
sys.stderr.write("BASE_URL is:\n%s\n\n" % BASE_URL)


@given('we have valid json alert output')
def step_impl(context):
    with open(results_file, 'r') as f:
        try:
            context.alerts = json.load(f)
        except Exception as e:
            sys.stdout.write('Error: Invalid JSON in %s: %s\n' %
                             (results_file, e))
            assert False


@given('the alert is on the correct base url')
def step_impl(context):
    pattern = re.compile(re.escape(BASE_URL), re.IGNORECASE)
    matches = list()

    for alert in context.alerts:
        if pattern.match(alert['url']) is not None:
            matches.append(alert)
    context.matches = matches
    assert True


@then('we should not have any "{error_name_value}" errors')
def check_for_errors_by_name(context, error_name_value):
    matches = list()
    for alert in context.alerts:
        alert_name = alert['name']
        if alert_name.lower() == error_name_value.lower():
            matches.append(alert)
    assert len(matches) == 0, loop_thru_messages(matches)



@step('I am on "{uri}"')
def get(context, uri):
    current_url = BASE_URL + uri
    context.driver.get(current_url)


@then('it should return a "{code}"')
def find_header(context, code):
    print ('Checking %s api status' % context.current_call)
    sys.stdout.write(str(context.current_call.status_code))
    assert context.current_call.status_code == int(code), 'Expected a %s for ' \
    'url \nInstead: %i' % (code, context.current_call.status_code)
