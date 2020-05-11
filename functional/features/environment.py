# -*- coding: UTF-8 -*-
import os
import sys
from behave import *
from qa.functional.features.browser import Browser
from qa.functional.features.steps.login import LoginPage
from qa.functional.features.steps.workarounds import LocalStorage
from qa.functional.features.requester import SetupRequests
from qa.settings import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NAME
from qa.settings import DEFAULT_WIDTH, DEFAULT_HEIGHT
from qa.settings import DISPLAY, XVFB_RESOLUTION
from qa.settings import EDITOR_EMAIL, EDITOR_PASSWORD, EDITOR_NAME
from qa.settings import HOST_URL, DRIVER, SELENIUM, IAP_ON, QA_ENV, log
from qa.settings import MOBILE_WIDTH, MOBILE_HEIGHT
from qa.settings import TABLET_WIDTH, TABLET_HEIGHT
from qa.settings import USER_EMAIL, USER_PASSWORD, USER_NAME
from selenium.webdriver.support.ui import WebDriverWait



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

def get_jira_number_from_tags(context):
    for tag in context.tags:
        if JIRA_PROJECT_ABBR in tag:
            return tag


def dismiss_cookie_consent(driver):
    local_storage = LocalStorage(driver)
    # Dismiss Cookie Consent Banner by Default
    local_storage.set('cookieConsent', 'true')


def clear_local_storage(driver):
    local_storage = LocalStorage(driver)
    local_storage.clear()


def is_not_chromedriver():
    return bool('chrome' not in DRIVER.lower())


# def before_all(context):
#     # If the environment is password protected you may have to login first.
#     context.browser = Browser()
#     context.driver = context.browser.get_browser_driver()
#     context.driver.get(HOST_URL)
#     email = ACCOUNTS['user']['email']
#     password = ACCOUNTS['user']['password']
#     name = ACCOUNTS['user']['name']
#     login = LoginPage(context.driver)
#     login.oauth_logic(email, password, name)
#

# def after_all(context):


def before_feature(context, feature):
    if 'server' in context.config.userdata:
        feature.name += ' on ' + context.config.userdata['server'] + ' environment'
        current_driver = str('tested_in_' + DRIVER)
        feature.tags.append(current_driver)


# def after_feature(context, feature):


def before_scenario(context, scenario):
    if 'skip' in context.tags:
        jira_number = get_jira_number_from_tags(context)
        scenario.skip("\n\tSkipping tests until %s is fixed" % jira_number)
        return
    if 'chrome-only' in context.tags:
        if is_not_chromedriver() is True:
            scenario.skip('Skipping test not supported outside chrome')
            return
    if 'no-safari' in context.tags:
        if 'safari' in DRIVER:
            scenario.skip('Skipping test not supported in safari')
            return
    if 'local-only' in context.tags:
        if QA_ENV != 'local':
            scenario.skip('Skipping test, only supported locally')
            return
    if 'no-local' in context.tags:
        if QA_ENV == 'local':
            scenario.skip('Skipping test, not supported locally')
            return
    if 'validity' in context.tags:
        # if sys.platform == 'darwin':
        log.debug('need to start xvfb to run outside headless')
        generated_command = 'Xvfb %s -screen 0 %s &' % (
            DISPLAY,
            XVFB_RESOLUTION
        )
        log.debug('Starting with command :\n%s' % str(generated_command))
        context.current_process = subprocess.Popen(
            [generated_command],
            stdout=subprocess.PIPE,
            shell=True
        )
        time.sleep(1)
        log.debug(
            'xvfb return code %s' % str(context.current_process.returncode)
        )
        assert 'command not found' not in str(context.current_process.stdout), \
            'xvfb could not be found, stdout:\n%s' % str(
                context.current_process.stdout
            )
        if IAP_ON is False:
            context.browser = Browser()
            log.info('Using local_html_validator for this test')
            context.driver = context.browser.get_driver_by_name('local_html_validator')
            assert context.driver.status_code == requests.codes.ok
        else:
            log.info('Using authenticated_local_html_validator for this test')
            context.browser = Browser(proxy=context.proxy, server=context.server, passthrough=PROXY_PASSTHROUGH)
            context.driver = context.browser.get_driver_by_name('authenticated_local_html_validator')
    elif 'browser' in context.tags:
        if IAP_ON is True:
            context.browser = Browser(proxy=context.proxy, server=context.server, passthrough=PROXY_PASSTHROUGH)
        else:
            context.browser = Browser()
        context.driver = context.browser.get_browser_driver()
        if 'chrome' in DRIVER:
            scenario.name += ' in %s %s' % (
                context.driver.capabilities['browserName'].capitalize(),
                context.driver.capabilities['browserVersion']
            )
        if 'firefox' in DRIVER:
            scenario.name += ' in %s %s' % (
                context.driver.capabilities['browserName'].capitalize(),
                context.driver.capabilities['browserVersion']
            )
    else:
        context.driver = None
    if 'requests' in context.tags:
        requester = SetupRequests()
        context.session = requester.setup_session()
    if context.driver is not None:
        context.wait = WebDriverWait(context.driver, 20, 0.25)
        if 'mobile' in context.tags:
            context.driver.set_window_size(MOBILE_WIDTH, MOBILE_HEIGHT)
        if 'tablet' in context.tags:
            context.driver.set_window_size(TABLET_WIDTH, TABLET_HEIGHT)
        if 'not-logged-in' in context.tags:
            delete_firebase_cookies(context.driver)


def after_scenario(context, scenario):
    if 'browser' in context.tags or 'validity' in context.tags:
        if ('skip' not in context.tags):
            if is_not_chromedriver() is True and 'chrome-only' in context.tags:
                return
            elif 'local-only' in context.tags and 'http://localhost:4444/wd/hub' != SELENIUM:
                return
            else:
                context.driver.quit()
