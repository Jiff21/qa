import os
import sys
from behave import *
from qa.analytics.features.browser import Browser


def before_scenario(context, feature):
    context.browser = Browser()
    context.driver = context.browser.get_browser_driver()


def after_scenario(context, feature):
    context.driver.quit()
