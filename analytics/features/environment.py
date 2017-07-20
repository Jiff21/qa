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
import sys
from behave import *
from qa.analytics.features.browser import Browser


def before_scenario(context, scenario):
    context.browser = Browser()
    context.driver = context.browser.get_browser_driver()


def after_scenario(context, feature):
    context.driver.quit()
