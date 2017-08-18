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
    context.current_node = context.results_json['audits']['aria-allowed-attr']['description'] \
        == 'Background and foreground colors have a sufficient contrast ratio', \
        'Contrast Ratio Json not found where expected'
    'Element aria-* attributes are allowed for this role'
    context.current_node = context.results_json['audits']['aria-allowed-attr']['score']
    assert True


@when('we find the contrast ratio section')
def step_impl(context):
    assert context.results_json['audits']['color-contrast']['name'] == \
        'color-contrast', 'Contrast Ratio Json not found where expected'
    context.current_node = context.results_json['audits']['color-contrast']['score']
    assert True


@when('we find the image-alt section')
def step_impl(context):
    assert context.results_json[
        'audits']['image-alt']['name'] == 'image-alt', \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['image-alt']['name'])
    )
    context.current_node = context.results_json[
        'audits']['image-alt']['name']
    assert True


@when('we find the form label section')
def step_impl(context):
    assert context.results_json['audits']['label']['name'] == 'label', \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['label']['name'])
    )
    context.current_node = context.results_json['audits']['label']['score']
    assert True
