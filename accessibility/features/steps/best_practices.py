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


def web_app_section(passed_json):
    new_json = passed_json['reportCategories'][0]
    return new_json


def best_practices(passed_json):
    new_json = passed_json['reportCategories'][3]
    return new_json


@when('we find the Redirects HTTP traffic to HTTPS section')
def step_impl(context):
    context.section = web_app_section(context.results_json)
    assert context.section['audits'][4]['result']['name'] == \
        'redirects-http', 'Did not get expected name'
    context.current_node = context.section['audits'][4]['result']['score']
    print (str(context.current_node) + '1')
    assert True


@when('we find the Has a <meta name="theme-color"> tag')
def step_impl(context):
    assert context.results_json[
        'audits']['themed-omnibox']['description'] == \
        'Address bar does not match brand colors'
    context.current_node = context.results_json[
        'audits']['themed-omnibox']['score']
    assert True


@when('we find the content is sized correctly for the viewport')
def step_impl(context):
    context.section = web_app_section(context.results_json)
    print(context.section['audits'][10]['id'])
    print(context.section['audits'][10]['result']['score'])
    assert context.section[
        'audits'][10]['id'] == \
        'content-width', "Did not get expected name"
    context.current_node = context.section[
        'audits'][10]['result']['score']
    assert True


@when('we find the Content with JavaScript disabled section')
def step_impl(context):
    assert context.results_json[
        'audits']['without-javascript']['description'] == \
        'Contains some content when JavaScript is not available'
    context.current_node = context.results_json[
        'audits']['without-javascript']['score']
    assert True


@when('we find the avoids document write section')
def step_impl(context):
    assert context.results_json[
        'audits']['no-document-write']['description'] == \
        'Avoids `document.write()`'
    context.current_node = context.results_json[
        'audits']['no-document-write']['score']
    assert True


@when('we find the noopener section')
def step_impl(context):
    context.section = best_practices(context.results_json)
    assert context.section['audits'][7]['result']['name'] == \
        'external-anchors-use-rel-noopener', 'Not expected name'
    context.current_node = context.section['audits'][7]['result']['score']
    assert True
