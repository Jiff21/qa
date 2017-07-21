'''
Feature: Our app is secure

  Scenario: Redirects http traffic to https

    Given we have valid json alert output
    When we find the Redirects HTTP traffic to HTTPS section
    Then aria should have be True
'''
import os
import json
import re
import sys
from behave import when, then
from qa.accessibility.features.environment import FILE_NAME
from qa.environment_variables import QA_FOLDER_PATH

results_file = '%saccessibility/output/%s.report.json' % (
    QA_FOLDER_PATH,
    FILE_NAME
)


@when('we find the Redirects HTTP traffic to HTTPS section')
def step_impl(context):
    assert context.results_json[
        'audits']['redirects-http']['description'] == \
        'Redirects HTTP traffic to HTTPS'
    context.current_node = context.results_json[
        'audits']['redirects-http']['score']
    assert True
