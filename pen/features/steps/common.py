import os
import json
import re
import sys
from behave import *
from qa.environment_variables import BASE_URL, QA_FOLDER_PATH

results_file = '%spen/results.json' % QA_FOLDER_PATH


@given('we have valid json alert output')
def step_impl(context):
    with open(results_file, 'r') as f:
        try:
            context.alerts = json.load(f)
        except Exception as e:
            sys.stdout.write('Error: Invalid JSON in %s: %s\n' %
                             (results_file, e))
            assert False


@when('the alert is on the correct base url')
def step_impl(context):
    pattern = re.compile(re.escape(BASE_URL), re.IGNORECASE)
    matches = list()

    for alert in context.alerts:
        if pattern.match(alert['url']) is not None:
            matches.append(alert)
    context.matches = matches
    assert True
