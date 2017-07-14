import os
import json
import re
import sys
from behave import *
from qa.accessibility.features.environment import FILE_NAME
from qa.environment_variables import BASE_URL, QA_FOLDER_PATH


results_file = '%saccessibility/output/%s.report.json' % (
    QA_FOLDER_PATH,
    FILE_NAME
)


@given('we have valid json alert output')
def step_impl(context):
    with open(results_file, 'r') as f:
        try:
            context.results_json = json.load(f)
        except Exception as e:
            sys.stdout.write('Error: Invalid JSON in %s: %s\n' %
                             (results_file, e))
            assert False
