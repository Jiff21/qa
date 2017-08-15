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
from qa.environment_variables import BASE_URL, CLIENT_ID
from qa.environment_variables import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NAME
from qa.environment_variables import EDITOR_EMAIL, EDITOR_PASSWORD, EDITOR_NAME
from qa.environment_variables import USER_EMAIL, USER_PASSWORD, USER_NAME
from qa.functional.features.browser import Browser
from qa.functional.features.steps.login import LoginPage
from qa.utilities.oauth.service_account_auth import make_iap_request

ACCOUNTS = {
    'admin': {
        'email': ADMIN_EMAIL,
        'password': ADMIN_PASSWORD,
        'name': ADMIN_NAME
    },
    'editor': {
        'email': EDITOR_EMAIL,
        'password': EDITOR_PASSWORD,
        'name': EDITOR_NAME
    },
    'user': {
        'email': USER_EMAIL,
        'password': USER_PASSWORD,
        'name': USER_NAME
    }
}

xml_js = '''
var req = new XMLHttpRequest();
req.open('GET', document.location, false);
req.setRequestHeader('Autorization', 'Bearer' + 'asdkbfbfdaiizdfbb');
req.send(null);
'''

# def before_all(context):
#     # If the environment is password protected you may have to login first.
#     context.browser = Browser()
#     context.driver = context.browser.get_browser_driver()
#     context.driver.get(BASE_URL)
#     email = ACCOUNTS['user']['email']
#     password = ACCOUNTS['user']['password']
#     name = ACCOUNTS['user']['name']
#     login = LoginPage(context.driver)
#     login.oauth_logic(email, password, name)
#

# def after_all(context):

# def before_feature(context, feature):
#
# def after_feature(context, feature):
#


def before_scenario(context, scenario):
    if 'browser' in context.tags:
        code, bearer_header = make_iap_request(BASE_URL, CLIENT_ID)
        # xml_js = '''
        # var req = new XMLHttpRequest();
        # req.open('GET', '%s', false);
        # req.setRequestHeader('Authorization', '%s');
        # req.send(null);
        # ''' % (BASE_URL, bearer_header['Authorization'])
        context.browser = Browser()
        context.driver = context.browser.get_browser_driver()
        # print(xml_js)
        context.driver.add_custom_request_header(
            "Authorization", "Bearer " + bearer_header["Authorization"])
        # context.driver.execute_script(xml_js)


def after_scenario(context, scenario):
    if 'browser' in context.tags:
        context.driver.quit()
