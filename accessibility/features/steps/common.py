import os
import json
import re
import sys
from behave import *
from environment_variables import BASE_URL, QA_FOLDER_PATH
from environment import FILE_NAME

FILE_NAME = os.getenv('FILE_NAME', 'example')

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
