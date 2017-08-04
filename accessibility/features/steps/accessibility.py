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


def accessibility_section(passed_json):
    new_json = passed_json['reportCategories'][2]
    return new_json


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
    context.section = accessibility_section(context.results_json)
    assert context.section['audits'][11]['id'] == \
        'color-contrast', 'Contrast Ratio Json not found where expected'
    context.current_node = context.section['audits'][11]['result']['score']
    assert True


@when('we find the image-alt section')
def step_impl(context):
    context.section = accessibility_section(context.results_json)
    assert context.section[
        'audits'][20]['id'] == 'input-image-alt', \
        'Did not get expected text instead:\n%s' % (
            str(context.section['audits'][20]['id'])
    )
    context.current_node = context.section[
        'audits'][20]['result']['score']
    assert True


@when('we find the form label section')
def step_impl(context):
    context.section = accessibility_section(context.results_json)
    assert context.section[
        'audits'][21]['id'] == 'label', \
        'Did not get expected text instead:\n%s' % (
            str(context.section['audits'][21]['id'])
    )
    context.current_node = context.section[
        'audits'][21]['result']['score']
    assert True
