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
from behave import before_all, after_all
from qa.e2e.features.browser import Browser
from selenium import webdriver
from applitools.eyes import Eyes
from qa.accounts import Accounts


def before_all(context):
    context.eyes = Eyes()
    context.eyes.api_key = Accounts.EYES_API_KEY
    context.browser = Browser()
    context.driver = context.driver.get_browser_driver()


def after_all(context):
    context.driver.quit()

    # Initialize the eyes SDK and set your private API key.
