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


@then('it should have an overall score above "{expected_score:f}"')
def score_over(context, expected_score):
    print (context.current_node)
    if context.current_node > expected_score:
        assert True
    else:
        sys.stderr.write(
            "Expected a score above %s for %s:\nInstead got %i" % (
                str(expected_score),
                FILE_NAME,
                context.current_node
            )
        )
        assert False


@then('it should have an overall score under "{expected_score:f}"')
def score_under(context, expected_score):
    print (context.current_node)
    if context.current_node < expected_score:
        assert True
    else:
        sys.stderr.write(
            "Expected a score under %s for %s:\nInstead got %i" % (
                str(expected_score),
                FILE_NAME,
                context.current_node
            )
        )
        assert False


@then('it should be "{true_or_false}"')
def bool_expect(context, true_or_false):
    print (context.current_node)
    if context.current_node == bool(true_or_false):
        sys.stderr.write(
            "Expected a value to be %s for %s:\n\tInstead got %i" % (
                true_or_false,
                FILE_NAME,
                context.current_node
            )
        )
        assert True
    else:
        assert False


# This should work but doesn't seem to be even if you run with --no-capture True flag
# Might be a bug as flag doesn't seem to do anything with -v printing settings
@then('we should warn if its not "{true_or_false}"')
def bool_expect(context, true_or_false):
    print (context.current_node)
    if context.current_node != bool(true_or_false):
        print ('FALSE')
        sys.stderr.write(
            "Expected a value to be %s for %s:\n\tInstead got %s" % (
                true_or_false,
                FILE_NAME,
                context.current_node
            )
        )


@then('it should be "{true_or_false}", and if not loop through fails')
def bool_expect(context, true_or_false):
    context.current_node = context.current_block['score']
    values = context.current_block['extendedInfo']['value']
    try:
        assert context.current_node == bool(true_or_false)
    except:
        sys.stderr.write('Found links missing noopener. \
            (For more information see https://developers.google.com/web/tools/lighthouse/audits/noopener)\n')
        sys.stderr.write('Found the following issues on %s:\n' % FILE_NAME)
        for value in values:
            sys.stderr.write(str(value))

        raise
