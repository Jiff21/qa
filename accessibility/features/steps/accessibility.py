'''
Feature: Our app follows accessibility best practices

  Scenario: Element aria-* attributes are allowed for this role

    Given we have valid json alert output
    When we find the aria-* attributes section
    Then aria should have be True

  Scenario: Background and foreground colors have a sufficient contrast ratio

    Given we have valid json alert output
    When we find the contrast ratio section
    Then contrast ratio should be True

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
    context.aria = context.results_json['audits']['aria-allowed-attr']['description'] \
        == 'Background and foreground colors have a sufficient contrast ratio', \
        'Contrast Ratio Json not found where expected'
    'Element aria-* attributes are allowed for this role'
    context.aria = context.results_json['audits']['aria-allowed-attr']['score']
    assert True


@then('aria should have be True')
def step_impl(context):
    assert context.aria == True, "Expected aria for %s to be True, instead %s" % (
        FILE_NAME,
        str(context.aria)
    )


@when('we find the contrast ratio section')
def step_impl(context):
    assert context.results_json[
        'audits']['color-contrast']['description'] == \
        'Background and foreground colors have a sufficient contrast ratio', \
        'Contrast Ratio Json not found where expected'
    context.contrast_ratio = context.results_json[
        'audits']['color-contrast']['score']
    assert True


@then('contrast ratio should be True')
def step_impl(context):
    assert context.contrast_ratio == True, "Expected Contrast Ratio for %s to be True, instead %s" % (
        FILE_NAME,
        str(context.contrast_ratio)
    )
