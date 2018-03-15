import os
import json
import re
import sys
from behave import when, then, given, step
from qa.settings import BASE_URL, QA_FOLDER_PATH

results_folder = '%svisual/results/' % QA_FOLDER_PATH

class LoopThroughException(Exception):

    def __init__(self, messages):
        self.value = ''
        for message in messages:
            self.value += '\r\n' + str(message)

    def __str__(self):
        return str(self.value)


@given('we find the json for "{page}" on "{browser}" for "{size}"')
def step_impl(context, page, browser, size):
    context.browser = browser.lower()
    context.size = size.lower()
    context.page = page.lower()
    results_test = context.page + '-on-' + context.size + '-device-in-' + context.browser + '-browser.json'
    sys.stderr.write('Looking for %s' % results_test)
    context.results_file = None
    for filename in os.listdir(results_folder):
        print(filename)
        if results_test in filename:
            context.results_file = results_folder + filename
            break
        else:
            continue
    assert context.results_file is not None, "did not find results file"

@given('it\'s valid json')
def step_impl(context):
    with open(context.results_file, 'r') as f:
        try:
            context.current_json = json.load(f)
        except Exception as e:
            sys.stdout.write('Error: Invalid JSON in %s: %s\n' %
                             (context.results_file, e))
            assert False


@given('we get the relevant json')
def step_impl(context):
    try:
        context.current_json = context.current_json['report']['nodes'][0]['nodes'][1]['nodes'][0]['sections'][0]['objects']
    except Exception as e:
        sys.stdout.write('Error: Could not find relevant json %s: %s\n' %
                         (context.current_json, e))
        assert False


@step('we loop get a list of objects')
def step_impl(context):
    context.objects = []
    for object in context.current_json:
        context.objects.append(object)

@step('we loop get a list of specs')
def step_impl(context):
    context.specs = []
    for spec in context.current_json:
        context.specs.append(spec['specs'])

@step('we make a list of errors')
def step_impl(context):
    context.errors = []
    for spec in context.specs:
        for certain_spec in spec:
            if certain_spec['status'] == 'error':
                context.errors.append("Visual Regression on %s %s for %s %s:\n%s" % (
                    BASE_URL,
                    context.page,
                    context.browser,
                    context.size,
                    certain_spec['errors']
                ))

@step('they should not have errors')
def step_impl(context):
    try:
        assert context.errors == []
    except:
        raise LoopThroughException(context.errors)
