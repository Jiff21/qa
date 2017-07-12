import os
import json
import re
import sys
from environment_variables import QA_FOLDER_PATH
from behave import *

results_file = '%spen/results.json' % QA_FOLDER_PATH

@then('we should not have X-Frame-Options Header Not Set alerts')
def step_impl(context):
    pattern = re.compile(r'X-Frame-Options', re.IGNORECASE)
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
