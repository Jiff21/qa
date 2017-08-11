import os
import sys
from behave import *
from qa.analytics.features.browser import Browser
from qa.environment_variables import BASE_URL
from qa.environment_variables import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NAME
from qa.environment_variables import EDITOR_EMAIL, EDITOR_PASSWORD, EDITOR_NAME
from qa.environment_variables import USER_EMAIL, USER_PASSWORD, USER_NAME
from qa.functional.features.steps.login import LoginPage
import time

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


def before_all(context):
    context.browser = Browser()
    context.driver = context.browser.get_browser_driver()
    context.driver.get(BASE_URL)
    print(USER_EMAIL)
    email = ACCOUNTS['user']['email']
    password = ACCOUNTS['user']['password']
    name = ACCOUNTS['user']['name']
    login = LoginPage(context.driver)
    login.oauth_logic(email, password, name)
    # context.cookies = context.driver.get_cookies()
    # for cookie in context.cookies:
    #     if cookie['name'] == 'GCP_IAAP_AUTH_TOKEN':
    #         context.session_cookie = cookie
    #     elif cookie['name'] == 'GCP_IAAP_XSRF_NONCE':
    #         context.xsrf_nonce = cookie
    #     else:
    #         print('these are not the droids (cookies) you\'re looking for')


def after_all(context):
    context.driver.quit()

#
# def before_scenario(context, feature):
#     context.browser = Browser()
#     context.driver = context.browser.get_browser_driver()
#
#
# def after_scenario(context, feature):
#     context.driver.quit()
