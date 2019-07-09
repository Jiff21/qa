import os
import json
import re
import sys
from behave import when, then
from qa.accessibility.features.environment import FILE_NAME
from qa.settings import QA_FOLDER_PATH
from common import results_file


@when('first meaningful paint section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['first-meaningful-paint']['title']
    context.expected_name = 'First Meaningful Paint'
    assert context.name == context.expected_name, \
        'Did not get expected Title, instead:\n\t%s' % (
            context.results_json[
                'audits']['first-meaningful-paint']['description']
        )
    context.current_node = context.results_json[
        'audits']['first-meaningful-paint']['numericValue']
    print (context.current_node)
    assert True


@when('we find the Time To Interactive')
def step_impl(context):
    context.name =  context.results_json['audits']['interactive']['id']
    context.expected_name = 'interactive'
    assert context.name == context.expected_name, \
        'Did not get expected name, instead:\n\t%s' % (
            context.results_json['audits']['interactive']['id']
            )
    context.current_node = context.results_json[
        'audits']['interactive']['numericValue']
    assert True


@when('we find the Unoptimized images section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['uses-optimized-images']['id']
    context.expected_name = 'uses-optimized-images'
    assert context.name == context.expected_name, \
        'Did not get expected name, instead:\n\t%s' % (
            context.results_json[
                'audits']['uses-optimized-images']['id']
            )
    context.current_node = context.results_json[
        'audits']['uses-optimized-images']['score']
    assert True


@when('we find the Render-blocking Resources section')
def step_impl(context):
    context.name = context.results_json[
            'audits']['render-blocking-resources']['id']
    context.expected_name = 'render-blocking-resources'
    assert context.name == context.expected_name, \
        'Did not get expected name, instead:\n\t%s' % (
            context.results_json[
                'audits']['render-blocking-resources']['id']
        )
    context.current_node = context.results_json[
        'audits']['render-blocking-resources']['score']
    assert True
