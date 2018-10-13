import os
import sys
from behave import *
from qa.functional.features.browser import Browser
from qa.functional.features.environment import get_jira_number_from_tags

def before_scenario(context, scenario):
    context.browser = Browser()
    context.driver = context.browser.get_browser_driver()
    if 'skip' in context.tags:
        jira_number = get_jira_number_from_tags(context)
        scenario.skip("\n\tSkipping tests until %s is fixed" % jira_number)
        return

def after_scenario(context, scenario):
    context.driver.quit()
