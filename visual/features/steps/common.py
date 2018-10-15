import os
import json
import re
import sys
from behave import when, then, given, step
from qa.settings import BASE_URL, QA_FOLDER_PATH
from qa.functional.features.steps.custom_exceptions import loop_thru_messages

results_folder = '%svisual/reports/' % QA_FOLDER_PATH


@given('we find the json for "{page}" on "{browser}" for "{size}"')
def step_impl(context, page, browser, size):
    context.browser = browser.lower()
    context.size = size.lower()
    context.page = page.replace(" ", "-").lower()
    results_test = context.page + '-on-' + context.size + '-device-in-' + context.browser + '-browser.json'
    print('Looking for %s' % results_test)
    context.results_file = None
    for filename in os.listdir(results_folder):
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
            context.original_json = json.load(f)
        except Exception as e:
            sys.stdout.write('Error: Invalid JSON in %s: %s\n' %
                             (context.results_file, e))
            assert False


@given('we get sections portion of the json')
def step_impl(context):
    try:
        context.section_json = context.original_json['report']['nodes'][0]['sections']
    except Exception as e:
        sys.stdout.write('Error: Could not find relevant json:\n\n%s\n\n%s\n' %
                         (context.original_json, e))
        raise

@step('and get the "{name}" section')
def step_impl(context, name):
    for section in context.section_json:
        if section['name'].lower() == name.lower():
            context.current_json = section['objects']
            break
        else:
            continue
    if not hasattr(context, 'current_json'):
    # if context.current_json is None:
        sys.stdout.write(
            'Error: Could not find section json:\n\n%s\n\n' %(
                context.section_json,
            )
        )
        raise


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
    assert context.errors == [], loop_thru_messages(context.errors)
    # try:
    #     assert context.errors == []
    # except:
    #     raise LoopThroughException(context.errors)
