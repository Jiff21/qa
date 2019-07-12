from behave import when, then, given, step
from qa.accessibility.features.environment import FILE_NAME
from qa.settings import QA_FOLDER_PATH
from common import results_file


@when('we find the Redirects HTTP traffic to HTTPS section')
def step_impl(context):
    context.name = context.results_json['audits']['redirects-http']['id']
    context.expected_name = 'redirects-http'
    assert context.name == context.expected_name, \
        'Did not get expected name for https traffic section'
    context.current_node = context.results_json[
        'audits']['redirects-http']['score']
    assert True


@step('we find the Has a themed-omnibox tag')
def step_impl(context):
    context.name = context.results_json[
        'audits']['themed-omnibox']['title']
    context.expected_name = 'Does not set an address-bar theme color'
    assert context.name == context.expected_name, \
        'Did not got expected title for brand colors'
    context.current_node = context.results_json[
        'audits']['themed-omnibox']['score']
    assert True


@when('we find the content is sized correctly for the viewport')
def step_impl(context):
    context.name = context.results_json['audits']['content-width']['id']
    context.expected_name = 'content-width'
    assert context.name == context.expected_name, \
        "Did not get expected name for context viewport"
    context.current_node = context.results_json[
        'audits']['content-width']['score']
    assert True


@when('we find the Content with JavaScript disabled section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['without-javascript']['title']
    context.expected_name = \
        'Contains some content when JavaScript is not available'
    assert context.name == context.expected_name, \
        'Did not get expected description for JavaScript Disabled'
    context.current_node = context.results_json[
        'audits']['without-javascript']['score']
    assert True


@when('we find the avoids document write section')
def step_impl(context):
    context.name = context.results_json['audits']['no-document-write']['id']
    context.expected_name = 'no-document-write'
    assert context.name == context.expected_name, \
        'Error locating Document Write Section'
    context.current_node = context.results_json[
        'audits']['no-document-write']['score']
    assert True


@when('we find the noopener section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['external-anchors-use-rel-noopener']['id']
    context.expected_name = 'external-anchors-use-rel-noopener'
    assert context.name == context.expected_name, \
        'Did not get expected name in noopener section'
    context.current_node = \
        context.results_json['audits']['external-anchors-use-rel-noopener']['score']
    assert True
