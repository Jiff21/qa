import os
import sys
from behave import *
from qa.functional.features.browser import Browser

#
# def before_all(context):
#
#
# def after_all(context):


# def before_feature(context, feature):

# def after_feature(context, feature):
#


def before_scenario(context, scenario):
    if os.getenv('DRIVER') == 'firefox':
        if "firefoxskip" in scenario.effective_tags:
            sys.stdout.write('firefox not supported for %s' % (scenario))
            scenario.mark_skipped()
    if 'browser' in context.tags:
        context.browser = Browser()
        context.driver = context.browser.get_browser_driver()


def after_scenario(context, feature):
    if 'browser' in context.tags:
        context.driver.quit()
