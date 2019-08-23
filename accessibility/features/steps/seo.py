import os
import json
import re
import sys
from behave import when, then
from qa.settings import QA_FOLDER_PATH


@when('we find the meta description section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['meta-description']['id']
    context.expected_name = 'meta-description'
    assert context.name == context.expected_name, \
        'Did not get expected id, instead:\n\t%s' % (
            context.results_json[
                'audits']['meta-description']['id']
        )
    context.current_node = context.results_json[
        'audits']['meta-description']['score']
    context.detailed_reason = '\n This is just generall good seo practices. ' \
        'meta description controls how search engines described the page. ' \
        'This is also one of those things that should only take a few minutes' \
        ' to fix. Checked by Magoo.\n'
    assert True


@when('we find the title tag section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['document-title']['id']
    context.expected_name = 'document-title'
    assert context.name == context.expected_name, \
        'Did not get expected ID, instead:\n\t%s' % (
            context.results_json[
                'audits']['document-title']['id']
        )
    context.current_node = context.results_json[
        'audits']['document-title']['score']
    context.detailed_reason = '\n This is just generally good seo practices. ' \
        'The <title> tag controls how search engines display the page.' \
        'This is also one of those things that should only take a few minutes' \
        ' to fix. Checked by Magoo.\n'
    assert True

@when('we find the meta-refresh section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['meta-refresh']['id']
    context.expected_name = 'meta-refresh'
    assert context.name == context.expected_name, \
        'Did not get expected ID, instead:\n\t%s' % (
            context.results_json[
                'audits']['meta-refresh']['id']
        )
    context.current_node = context.results_json[
        'audits']['meta-refresh']['score']
    context.detailed_reason = '\n The document should not refresh to redirect ' \
    'traffic. Checked by Magoo.\n'
    assert True
