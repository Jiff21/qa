'''
Feature: Our app performs well

  Scenario: The application can load over a flaky connection

    Given we have valid json alert output
    When we find the flaky connection section
    Then it should have an overall score above "80"
'''
import os
import json
import re
import sys
from environment_variables import QA_FOLDER_PATH
from behave import *

FILE_NAME = 'example'

results_file = '%saccessibility/output/%s.report.json' % (
    QA_FOLDER_PATH,
    FILE_NAME
)

@when('we find the flaky connection section')
def step_impl(context):
    # pattern = re.compile(re.escape(BASE_URL), re.IGNORECASE)
    context.aggregations = context.results_json['aggregations']
    flaky = {}
    for item in context.aggregations:
        if item['name'] == 'App can load on offline/flaky connections':
            flaky[item]
    context.flaky = flaky
    # pattern = re.compile(re.escape(BASE_URL), re.IGNORECASE)
    # matches = list()
    #
    # for alert in context.alerts:
    #     if pattern.match(alert['url']) is not None:
    #         matches.append(alert)
    # context.matches = matches
    assert True


@then('it should have an overall score above "{score}"')
def step_impl(context, score):
    if context.flaky['overall'] < score:
        sys.stderr.write(
            "Expected a %s score above %i:\nInstead got %i" % (
                context.flaky['name'],
                score,
                ontext.flaky['overall']
                )
            )
        assert False
    else:
        assert True
