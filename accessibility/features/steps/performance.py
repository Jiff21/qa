'''
Feature: Our app performs well

  Scenario: First meaningful paint is less than half a second
    Given we have valid json alert output
    When first meaningful paint section
    Then it should have an overall score under "5000.0"

  Scenario: Time To Interactive under one second
    Given we have valid json alert output
    When we find the Time To Interactive
    Then it should have an overall score under "1000.0"

  Scenario: Does not use document write
    Given we have valid json alert output
    When we find the Avoids document.write()
    Then it should be "True"

  Scenario: We should avoid Optimized Images
    Given we have valid json alert output
    When we find the Unoptimized images section
    Then we should warn if its not "True"

  Scenario: We should avoid Render-blocking Stylesheets
    Given we have valid json alert output
    When we find the Render-blocking Stylesheets section
    Then we should warn if its not "True"

  Scenario: We should avoid Render-blocking scripts
    Given we have valid json alert output
    When we find the Render-blocking scripts section
    Then we should warn if its not "True"

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


@when('first meaningful paint section')
def step_impl(context):
    assert context.results_json[
        'audits']['first-meaningful-paint']['description'] == \
        'First meaningful paint', \
        'Did not get expected description, instead:\n\t%s' % (
            context.results_json[
                'audits']['first-meaningful-paint']['description']
    )
    context.current_node = context.results_json[
        'audits']['first-meaningful-paint']['rawValue']
    print (context.current_node)
    assert True


@when('we find the Time To Interactive')
def step_impl(context):
    assert context.results_json[
        'audits']['time-to-interactive']['description'] == \
        'Time To Interactive (alpha)', \
        'Did not get expected description, instead:\n\t%s' % (
            context.results_json[
                'audits']['first-meaningful-paint']['description']
    )
    context.current_node = context.results_json[
        'audits']['time-to-interactive']['rawValue']
    assert True


@when('we find the Unoptimized images section')
def step_impl(context):
    assert context.results_json[
        'audits']['uses-optimized-images']['description'] == \
        'Unoptimized images', \
        'Did not get expected description, instead:\n\t%s' % (
            context.results_json[
                'audits']['uses-optimized-images']['description']
    )
    context.current_node = context.results_json[
        'audits']['uses-optimized-images']['rawValue']
    assert True


@when('we find the Render-blocking Stylesheets section')
def step_impl(context):
    assert context.results_json[
        'audits']['link-blocking-first-paint']['description'] == \
        'Render-blocking Stylesheets', \
        'Did not get expected description, instead:\n\t%s' % (
            context.results_json[
                'audits']['link-blocking-first-paint']['description']
    )
    context.current_node = context.results_json[
        'audits']['link-blocking-first-paint']['rawValue']
    assert True


@when('we find the Render-blocking scripts section')
def step_impl(context):
    assert context.results_json[
        'audits']['script-blocking-first-paint']['description'] == \
        'Render-blocking scripts', \
        'Did not get expected description, instead:\n\t%s' % (
        context.results_json[
            'audits']['script-blocking-first-paint']['description']
    )
    context.current_node = context.results_json[
        'audits']['script-blocking-first-paint']['rawValue']
    assert True
