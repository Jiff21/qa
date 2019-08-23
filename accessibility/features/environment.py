import os
from qa.functional.features.environment import get_jira_number_from_tags

def before_all(context):
    file_path = os.path.abspath(os.path.dirname(__file__))
    page_report_path = os.path.normpath('../../../../%saccessibility/output/')
    context.directory = os.path.join(
        file_path,
        page_report_path

    )
    context.detailed_reason = ''

def before_scenario(context, scenario):
    if 'skip' in context.tags:
        jira_number = get_jira_number_from_tags(context)
        scenario.skip("\n\tSkipping tests until %s is fixed" % jira_number)
        return
    if 'warn' in context.tags:
        # Set to immediately out rather than keep for fail
        context.stdout_capture = False
        context.stderr_capture = False


def after_scenario(context, scenario):
    if 'warn' in context.tags:
        context.stdout_capture = True
        context.stderr_capture = True
