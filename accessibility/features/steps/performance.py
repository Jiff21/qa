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
        'audits']['first-meaningful-paint']['description']
    context.expected_name = 'First meaningful paint'
    assert context.name == context.expected_name, \
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
    context.name =  context.results_json['audits']['first-interactive']['name']
    context.expected_name = 'first-interactive'
    assert context.name == context.expected_name, \
        'Did not get expected name, instead:\n\t%s' % (
            context.results_json['audits']['first-interactive']['name']
            )
    context.current_node = context.results_json[
        'audits']['first-interactive']['rawValue']
    assert True


@when('we find the Unoptimized images section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['uses-optimized-images']['name']
    context.expected_name = 'uses-optimized-images'
    assert context.name == context.expected_name, \
        'Did not get expected name, instead:\n\t%s' % (
            context.results_json[
                'audits']['uses-optimized-images']['name']
            )
    context.current_node = context.results_json[
        'audits']['uses-optimized-images']['score']
    assert True


@when('we find the Render-blocking Stylesheets section')
def step_impl(context):
    context.name = context.results_json[
        'audits']['link-blocking-first-paint']['name']
    context.expected_name ='link-blocking-first-paint'
    assert context.name == context.expected_name, \
        'Did not get expected name, instead:\n\t%s' % (
            context.results_json[
                'audits']['link-blocking-first-paint']['name']
        )
    context.current_node = context.results_json[
        'audits']['link-blocking-first-paint']['score']
    assert True


@when('we find the Render-blocking scripts section')
def step_impl(context):
    context.name = context.results_json[
            'audits']['script-blocking-first-paint']['name']
    context.expected_name = 'script-blocking-first-paint'
    assert context.name == context.expected_name, \
        'Did not get expected name, instead:\n\t%s' % (
            context.results_json[
                'audits']['script-blocking-first-paint']['name']
        )
    context.current_node = context.results_json[
        'audits']['script-blocking-first-paint']['score']
    assert True
