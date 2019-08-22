import os
import json
import re
import sys
from qa.accessibility.features.environment import FILE_NAME
from qa.settings import QA_FOLDER_PATH
from behave import when, then


@when('we find the aria-* attributes section')
def step_impl(context):
    context.name = context.results_json['audits']['aria-allowed-attr']['id']
    context.expected_name = 'aria-allowed-attr'
    assert context.name == context.expected_name, \
         'Did not find aria-allowed-attr section'
    context.current_node = context.results_json['audits']['aria-allowed-attr']['score']
    assert True


@when('we find the contrast ratio section')
def step_impl(context):
    context.name = context.results_json['audits']['color-contrast']['id']
    context.expected_name = 'color-contrast'
    assert context.name == context.expected_name, 'Contrast Ratio Json not found where expected'
    context.current_node = context.results_json['audits']['color-contrast']['score']
    assert True


@when('we find the image-alt section')
def step_impl(context):
    context.name = context.results_json['audits']['image-alt']['id']
    context.expected_name = 'image-alt'
    assert context.name == context.expected_name, \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['image-alt']['name'])
        )
    context.current_node = context.results_json['audits']['image-alt']['score']
    assert True


@when('we find the form label section')
def step_impl(context):
    context.name = context.results_json['audits']['label']['id']
    context.expected_name = 'label'
    assert context.name == context.expected_name, \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['label']['name'])
        )
    context.current_node = context.results_json['audits']['label']['score']
    assert True
