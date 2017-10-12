import os
from behave import *
from qa.settings import BASE_URL
from qa.settings import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NAME
from qa.settings import EDITOR_EMAIL, EDITOR_PASSWORD, EDITOR_NAME
from qa.settings import USER_EMAIL, USER_PASSWORD, USER_NAME

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
        context.browser = Browser()
        context.driver = context.browser.get_browser_driver()


def after_scenario(context, scenario):
    if 'browser' in context.tags:
        context.driver.quit()
