import os
import json
import re
import sys
from behave import *
from environment_variables import BASE_URL
results_file = 'pen/results.json'

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


@when('the alert is on the correct base url')
def step_impl(context):
    pattern = re.compile(re.escape(BASE_URL), re.IGNORECASE)
    matches = list()

    for alert in context.alerts:
        if pattern.match(alert['url']) is not None:
            matches.append(alert)
    context.matches = matches
    assert True
