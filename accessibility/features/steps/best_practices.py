'''
Feature: Our app is secure

  Scenario: Redirects http traffic to https
    Given we have valid json alert output
    When we find the Redirects HTTP traffic to HTTPS section
    Then it should be "True"

  @stdout-all
  Scenario: If we have time we should support theme-color nav bars
    Given we have valid json alert output
    When we find the Has a <meta name="theme-color"> tag
    Then we should warn if its not "True"

  Scenario: Should be mobile friendly
    Given we have valid json alert output
    When we find the content is sized correctly for the viewport
    Then it should be "True"

  Scenario: Contains some content when JavaScript is not available
    Given we have valid json alert output
    When we find the Content with JavaScript disabled section
    Then it should be "True"

  Scenario: Does not use document write
    Given we have valid json alert output
    When we find the avoids document write section
    Then it should be "True"

  Scenario: Target _blank links use rel='noopener'
    Given we have valid json alert output
    When we find the noopener section
    Then it should be "True"
'''
from behave import when, then, given, step
from qa.accessibility.features.environment import FILE_NAME
from qa.environment_variables import QA_FOLDER_PATH

results_file = '%saccessibility/output/%s.report.json' % (
    QA_FOLDER_PATH,
    FILE_NAME
)


@when('we find the Redirects HTTP traffic to HTTPS section')
def step_impl(context):
    context.name = context.results_json['audits']['redirects-http']['name']
    context.expected_name = 'redirects-http'
    assert context.name == context.expected_name, \
        'Did not get expected name for https traffic section'
    context.current_node = context.results_json[
        'audits']['redirects-http']['score']
    assert True


@when('we find the Has a <meta name="theme-color"> tag')
def step_impl(context):
    context.name = context.results_json[
        'audits']['themed-omnibox']['description']
    context.expected_name = 'Address bar does not match brand colors'
    assert context.name == context.expected_name, \
        'Did not got expected description for brand colors'
    context.current_node = context.results_json[
        'audits']['themed-omnibox']['score']
    assert True


@when('we find the content is sized correctly for the viewport')
def step_impl(context):
    context.name = context.results_json['audits']['content-width']['name']
    context.expected_name = 'content-width'
    assert context.name == context.expected_name, \
        "Did not get expected name for context viewport"
    context.current_node = context.results_json[
        'audits']['content-width']['score']
    assert True


@when('we find the Content with JavaScript disabled section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['without-javascript']['description']
    context.expected_name = \
        'Contains some content when JavaScript is not available'
    assert context.name == context.expected_name, \
        'Did not get expected description for JavaScript Disabled'
    context.current_node = context.results_json[
        'audits']['without-javascript']['score']
    assert True


@when('we find the avoids document write section')
def step_impl(context):
    context.name = context.results_json['audits']['no-document-write']['name']
    context.expected_name = 'no-document-write'
    assert context.name == context.expected_name, \
        'Error locating Document Write Section'
    context.current_node = context.results_json[
        'audits']['no-document-write']['score']
    assert True


@when('we find the noopener section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['external-anchors-use-rel-noopener']['name']
    context.expected_name = 'external-anchors-use-rel-noopener'
    assert context.name == context.expected_name, \
        'Did not get expected name in noopener section'
    context.current_node = \
        context.results_json['audits']['external-anchors-use-rel-noopener']['score']
    assert True

