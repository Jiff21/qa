'''
Feature: Our app is secure

  Scenario: Redirects http traffic to https
    Given we have valid json alert output
    When we find the Redirects HTTP traffic to HTTPS section
    Then it should be "True"

  Scenario: If we have time we should support theme-color nav bars
    Given we have valid json alert output
    When we find the Has a <meta name="theme-color"> tag
    Then we should warn if its not "True"

  Scenario: Contains some content when JavaScript is not available
    Given we have valid json alert output
    When we find the Content with JavaScript disabled section
    Then it should be "True"

  Scenario: Does not use document write
    Given we have valid json alert output
    When we find the Avoids document.write() section
    Then it should be "True"

  Scenario: Target _blank links use rel='noopener'
    Given we have valid json alert output
    When we find the noopener section
    Then it should be "True"

'''
import os
import json
import re
import sys
from behave import when, then
from qa.accessibility.features.environment import FILE_NAME
from qa.environment_variables import QA_FOLDER_PATH

results_file = '%saccessibility/output/%s.report.json' % (
    QA_FOLDER_PATH,
    FILE_NAME
)


@when('we find the Redirects HTTP traffic to HTTPS section')
def step_impl(context):
    assert context.results_json[
        'audits']['redirects-http']['description'] == \
        'Redirects HTTP traffic to HTTPS'
    context.current_node = context.results_json[
        'audits']['redirects-http']['score']
    assert True


@when('we find the Has a <meta name="theme-color"> tag')
def step_impl(context):
    assert context.results_json[
        'audits']['theme-color-meta']['description'] == \
        'Has a `<meta name=\"theme-color\">` tag'
    context.current_node = context.results_json[
        'audits']['theme-color-meta']['score']
    assert True


@when('we find the Content is sized correctly for the viewport')
def step_impl(context):
    assert context.results_json[
        'audits']['content-width']['description'] == \
        'Content is sized correctly for the viewport'
    context.current_node = context.results_json[
        'audits']['content-width']['score']
    assert True


@when('we find the Content with JavaScript disabled section')
def step_impl(context):
    assert context.results_json[
        'audits']['without-javascript']['description'] == \
        'Contains some content when JavaScript is not available'
    context.current_node = context.results_json[
        'audits']['without-javascript']['score']
    assert True


@when('we find the Avoids document.write() section')
def step_impl(context):
    assert context.results_json[
        'audits']['no-document-write']['description'] == \
        'Avoids `document.write()`'
    context.current_node = context.results_json[
        'audits']['no-document-write']['score']
    assert True


@when('we find the noopener section')
def step_impl(context):
    assert context.results_json[
        'audits']['external-anchors-use-rel-noopener']['description'] == \
        'Opens external anchors using rel=\"noopener\"'
    context.current_block = context.results_json[
        'audits']['external-anchors-use-rel-noopener']
    assert True
