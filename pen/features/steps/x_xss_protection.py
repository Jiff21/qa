import os
import json
import re
import sys

from behave import *

results_file = 'pen/results.json'


@then('we should not have X-XSS-Protection Header Not Set alerts')
def step_impl(context):
    pattern = re.compile(r'X-XSS-Protection', re.IGNORECASE)
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
    if len(matches) > 0:
        assert False
    else:
        assert True
