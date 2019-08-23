import os
import json
import re
import sys
from behave import when, then
from qa.settings import QA_FOLDER_PATH


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


@when('we find the total weight section')
def step_impl(context):
    context.name = context.results_json[
            'audits']['total-byte-weight']['id']
    context.expected_name = 'total-byte-weight'
    assert context.name == context.expected_name, \
        'Did not get expected name, instead:\n\t%s' % (
            context.results_json[
                'audits']['render-blocking-resources']['id']
        )
    context.current_node = context.results_json[
        'audits']['total-byte-weight']['numericValue']
    context.total_kb = round(context.current_node / 1000)
    context.detailed_reason = '\n This is generally goood for page speed. '\
        'Checked by Magoo.\n'
    assert True


@step('we check to see make sure its under {num} kb')
def step_impl(context, num):
    assert context.total_kb < num, 'Expected resources to be under %dkb but ' \
        'got a size of %dkb' % (num, context.total_kb)
