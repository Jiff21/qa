import json
import os
import sys
from behave import when, then, given, step
# from qa.accessibility.features.environment import context.page_name
from qa.settings import log, HOST_URL, QA_FOLDER_PATH



@given('we load lighthouse results file "{page_name}"."{format}"')
def step_impl(context, page_name, format='json'):
    context.page_name = page_name.lower().replace(' ', '_')
    file_path = os.path.abspath(os.path.dirname(__file__))
    page_report_path = os.path.normpath(
        '../../../../%s/accessibility/output/%s.report.%s' % (
            QA_FOLDER_PATH,
            context.page_name,
            format
        )
    )
    context.current_report = os.path.join(
        file_path,
        page_report_path

    )
    print(os.path.relpath)
    log.debug('Getting json from %s' % context.current_report)
    print(type(context.current_report))
    with open(context.current_report, 'r') as f:
        try:
            log.debug('Loading %s' % format)
            context.results_json = json.load(f)
        except Exception as e:
            sys.stdout.write(
                'Error: Invalid JSON in %s: %s\n' % (
                    context.current_report,
                    e
                )
            )
            assert False



@then('it should have a score value of "{expected_score:d}"')
def score_over(context, expected_score):
    log.debug(context.current_node)
    if context.current_node == expected_score:
        assert True
    else:
        sys.stderr.write(
            "Expected a score above %s for %s:\nInstead got %i" % (
                str(expected_score),
                context.page_name,
                context.current_node,
                context.detailed_reason
            )
        )
        assert False


@then('it should have an overall score above "{expected_score:f}"')
def score_over(context, expected_score):
    log.debug(context.current_node)
    if context.current_node > expected_score:
        assert True
    else:
        sys.stderr.write(
            "Expected a score above %s for %s:\nInstead got %i%s" % (
                str(expected_score),
                context.page_name,
                context.current_node,
                context.detailed_reason
            )
        )
        assert False

@then('it should have an overall score under "{expected_score:f}"')
def score_under(context, expected_score):
    log.debug(context.current_node)
    if context.current_node < expected_score:
        assert True
    else:
        sys.stderr.write(
            "Expected a score under %s for %s:\nInstead got %s%s" % (
                str(expected_score),
                context.page_name,
                context.current_node,
                context.detailed_reason
            )
        )
        assert False


@then('it should be "{true_or_false}"')
def bool_expect(context, true_or_false):
    expectation_to_bool = bool(true_or_false)
    assert context.current_node == expectation_to_bool, \
        'Expected a value to be %s for %s:\n\tInstead got %s%s' % (
            expectation_to_bool,
            context.page_name,
            context.current_node,
            context.detailed_reason
        )


@then('we should warn if its not "{true_or_false}"')
def bool_expect2(context, true_or_false):
    expectation_to_bool = bool(true_or_false)
    if context.current_node != true_or_false:
        # Note, if you don't include a \n at end of print it will get
        # overwritten in terminal
        print('\033[93m' +
               'Expected a value to be %s for %s:\n\tInstead got %s\n\n' % (
                   expectation_to_bool,
                   context.page_name,
                   context.current_node
               ) + '\033[00m'
               )
    else:
        assert 1 == 1, context.detailed_reason


@then('we should warn if score is below "{number:d}"')
def warn_number(context, number):
    if context.current_node < number:
        print('\033[93m' +
               'Expected a value to be above %d for %s:\n\tInstead got %s' % (
                   number,
                   context.page_name,
                   context.current_node
               ) + '\033[00m'
               )
    else:
        assert 1 == 1, context.detailed_reason


@then('it should be "{true_or_false}", and if not loop through fails')
def bool_expect3(context, true_or_false):
    context.score_node = context.current_block['score']
    values = context.current_block['extendedInfo']['value']
    try:
        assert context.score_node == bool(true_or_false)
    except:
        sys.stderr.write('Found links missing noopener. \
            (For more information see https://developers.google.com/web/tools/lighthouse/audits/noopener)\n')
        sys.stderr.write('Found the following issues on %s:\n' % context.page_name)
        for value in values:
            sys.stderr.write(str(value))
        print(context.detailed_reason)
        raise
