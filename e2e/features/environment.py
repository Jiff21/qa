# -*- coding: UTF-8 -*-
'''
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.
before_tag(context, tag), after_tag(context, tag)
'''

import os
from behave import *
from qa.e2e.features.browser import Browser

#
# def before_feature(context, feature):
#     if 'browser' in feature.tags:
#         context.browser = Browser()
#         context.browser = context.browser.get_browser_driver()
#
#
# def after_feature(context, feature):
#     if 'browser' in feature.tags:
#         context.browser.quit()


def before_all(context):
    context.browser = Browser()
    context.browser = context.browser.get_browser_driver()


def after_all(context):
    context.browser.quit()
