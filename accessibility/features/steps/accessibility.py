import os
import json
import re
import sys
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
    context.detailed_reason = '\n This is WGAC2.1 (AA) Mandatory so unless its ' \
        'a false positive we are contractually obligated to do this. It also ' \
        'shows up in that one tool. Checked by Magoo.' \
        '\nhttps://www.w3.org/TR/WCAG21/#contrast-minimum\n'


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
    context.detailed_reason = '\nWGAC2.1 mandates img tags have alt  text ' \
        'We are contractually obligated to do this. If the  image doesn\'t add'\
        ' context the correct way to do this is change it to a div with a ' \
        ' background image so screen readers ignore it. Checked by Magoo.' \
        '\nhttps://www.w3.org/TR/WCAG21/#non-text-content\n'


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


@when('we find the duplicate-id label section')
def step_impl(context):
    context.name = context.results_json['audits']['duplicate-id']['id']
    context.expected_name = 'duplicate-id'
    assert context.name == context.expected_name, \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['duplicate-id']['id'])
        )
    context.current_node = context.results_json['audits']['duplicate-id']['score']
    assert True
    context.detailed_reason = '\nWGAC2.1 (A) mandates that IDs are unique for ' \
    'html parsing purposes. Also duplciate IDs are invalid HTML. Checked by Magoo.' \
    '\nhttps://www.w3.org/WAI/WCAG21/quickref/?versions=2.1#qr-ensure-compat-parses\n'


@when('we find the html-has-lang section')
def step_impl(context):
    context.name = context.results_json['audits']['html-has-lang']['id']
    context.expected_name = 'html-has-lang'
    assert context.name == context.expected_name, \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['html-has-lang']['id'])
        )
    context.current_node = context.results_json['audits']['html-has-lang']['score']
    assert True
    context.detailed_reason = '\nWGAC2.1 (A) mandates that <html lang="XX"> ' \
    'gets set. We are contractually obligated to do this. Checked by Magoo.' \
    '\nhttps://www.w3.org/TR/WCAG21/#language-of-page\n'


@when('we find the meta-viewport section')
def step_impl(context):
    context.name = context.results_json['audits']['meta-viewport']['id']
    context.expected_name = 'meta-viewport'
    assert context.name == context.expected_name, \
        'Did not get expected text instead:\n%s' % (
            str(context.results_json['audits']['meta-viewport']['id'])
        )
    context.current_node = context.results_json['audits']['meta-viewport']['score']
    assert True
    context.detailed_reason = '\nWGAC2.1 (AA) mandates that the user ' \
    'can zoom without losing functionality. Also note that 2.1 requires you to '\
    'only need to scroll horizontally or vertially, but not both. Checked by Magoo.' \
    '\nhttps://www.w3.org/TR/WCAG21/#reflow\n'
