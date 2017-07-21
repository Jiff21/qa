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


@then('it should have an overall score above "{expected_score}"')
def score_expect(context, expected_score):
    print (context.current_node)
    if context.current_node < float(expected_score):
        sys.stderr.write(
            "Expected a score above %s for %s:\nInstead got %i" % (
                expected_score,
                FILE_NAME,
                context.current_node
            )
        )
        assert False
    else:
        assert True


@then('it should be "{true_or_false}"')
def bool_expect(context, true_or_false):
    print (context.current_node)
    if context.current_node == bool(true_or_false):
        sys.stderr.write(
            "Expected a value to be %s for %s:\nInstead got %i" % (
                true_or_false,
                FILE_NAME,
                context.current_node
            )
        )
        assert True
    else:
        assert False
