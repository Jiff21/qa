import os
import json
import re
import sys

from behave import *

results_file = 'pen/results.json'


@given('we have valid json alert output')
def step_impl(context):
    with open(results_file, 'r') as f:
        try:
            context.alerts = json.load(f)
        except Exception as e:
            sys.stdout.write('Error: Invalid JSON in %s: %s\n' %
                             (results_file, e))
            assert False


@then('We should not have X-Content-Type-Options alerts')
def step_impl(context):
    pattern = re.compile(r'X-Content-Type-Options', re.IGNORECASE)
    matches = list()
    for alert in context.alerts:
        if pattern.match(alert['alert']) is not None:
            matches.append(alert)

    if len(matches) > 0:
        sys.stderr.write("The following alerts failed:\n")
    for risk in matches:
        sys.stderr.write("\tConfidence: %s\n\turl: %s   %s\n" % (
            risk['confidence'],
            risk['method'],
            risk['url']
        ))
        assert False
    else:
        assert True
