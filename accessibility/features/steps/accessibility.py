'''
Feature: Our app follows accessibility best practices

  Scenario: Element aria-* attributes are allowed for this role
    Given we have valid json alert output
    When we find the aria-* attributes section
    Then it should be "True"

  Scenario: Background and foreground colors have a sufficient contrast ratio
    Given we have valid json alert output
    When we find the contrast ratio section
    Then it should be "True"

  Scenario: Every image element has an alt attribute
    Given we have valid json alert output
    When we find the image-alt section
    Then it should be "True"

  Scenario: Every form element has a label
    Given we have valid json alert output
    When we find the form label section
    Then it should be "True"
'''
import os
import json
import re
import sys
from qa.accessibility.features.environment import FILE_NAME
from qa.environment_variables import QA_FOLDER_PATH
from behave import when, then


results_file = '%saccessibility/output/%s.report.json' % (
    QA_FOLDER_PATH,
    FILE_NAME
)


@when('we find the aria-* attributes section')
def step_impl(context):
    context.name = context.results_json['audits']['aria-allowed-attr']['name']
    context.expected_name = 'aria-allowed-attr'
    assert context.name == context.expected_name, \
         'Did not find aria-allowed-attr section'
    context.current_node = context.results_json['audits']['aria-allowed-attr']['score']
    assert True


@when('we find the contrast ratio section')
def step_impl(context):
    context.name = context.results_json['audits']['color-contrast']['name']
    context.expected_name = 'color-contrast'
    assert context.name == context.expected_name, 'Contrast Ratio Json not found where expected'
    context.current_node = context.results_json['audits']['color-contrast']['score']
    assert True


@when('we find the image-alt section')
def step_impl(context):
    context.name = context.results_json['audits']['image-alt']['name']
    context.expected_name = 'image-alt'
    assert context.name == context.expected_name, \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['image-alt']['name'])
        )
    context.current_node = context.results_json['audits']['image-alt']['score']
    assert True


@when('we find the form label section')
def step_impl(context):
    context.name = context.results_json['audits']['label']['name']
    context.expected_name = 'label'
    assert context.name == context.expected_name, \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['label']['name'])
        )
    context.current_node = context.results_json['audits']['label']['score']
    assert True
