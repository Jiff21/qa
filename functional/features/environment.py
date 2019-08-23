# -*- coding: UTF-8 -*-
import logging
import json
import os
import requests
import sys
import time
from behave import *
from qa.settings import HOST, HOST_URL, DRIVER, SELENIUM, PAGES_DICT
from qa.settings import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NAME
from qa.settings import EDITOR_EMAIL, EDITOR_PASSWORD, EDITOR_NAME
from qa.settings import USER_EMAIL, USER_PASSWORD, USER_NAME, FIREBASE_KEY
from qa.settings import ACCOUNTS, default_headers
from qa.settings import DEFAULT_WIDTH, DEFAULT_HEIGHT
from qa.settings import MOBILE_WIDTH, MOBILE_HEIGHT
from qa.settings import TABLET_WIDTH, TABLET_HEIGHT
from qa.settings import HOST, HOST_URL, CLIENT_ID, IAP_ON

# from qa.functional.features.browser import Browser
from qa.functional.features.steps.login import LoginPage
from qa.functional.features.steps.workarounds import LocalStorage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from browsermobproxy import Server, Client
from qa.functional.features.browsermob_browser import Browser
from qa.utilities.oauth.service_account_auth import make_iap_request
from qa.functional.features.requester import SetupRequests


logging.basicConfig()


def get_proxy_and_server(passed_dict):
    print('Getting Browsermob proxy and server')
    server = Server(
        'qa/env/bin/browsermob-proxy/bin/browsermob-proxy',
        options={'existing_proxy_port_to_use': 8999}
    )
    server.start()
    proxy = server.create_proxy()
    proxy.headers({"Authorization": passed_dict["Authorization"]})
    proxy.new_har(HOST)
    return proxy, server


def get_jira_number_from_tags(context):
    for tag in context.tags:
        if 'RTK-' in tag:
            return tag


def set_logged_in_before(driver):
    local_storage = LocalStorage(driver)
    local_storage.set('sitekit:tour:%s' % HOST, 1)


class SiteLogin:


    def __init__(self, driver) :
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40, 0.25)
        self.local_storage = LocalStorage(self.driver)
        self.login_button = (By.XPATH, '(//div[@id="firebaseui-auth-container"]//li)[2]/button')
        self.email_field = (By.XPATH, '//input[@name="email"]')
        self.password_field = (By.XPATH, '//input[@name="password"]')
        self.submit_button = (By.XPATH, '//button[@type="submit"]')



    def __len__(self):
        return self.driver.execute_script("return window.localStorage.length;")


    def click_login_button(self) :
        email_login_button = self.wait.until(
            EC.element_to_be_clickable((self.login_button))
        )
        email_login_button.click()


    def type_email(self, user_name) :
        email_field = self.wait.until(
            EC.element_to_be_clickable((self.email_field))
        )
        if 'user' in user_name:
            email_field.send_keys(USER_EMAIL)
        elif 'editor' in user_name:
            email_field.send_keys(EDITOR_EMAIL)
        elif 'admin' in user_name:
            email_field.send_keys(ADMIN_EMAIL)
        else:
            assert 1 == 2, 'Unrecognized user name'


    def click_submit(self) :
        email_login_button = self.wait.until(
            EC.element_to_be_clickable((self.submit_button))
        )
        email_login_button.click()


    def type_password(self, user_name) :
        password_field = self.wait.until(
            EC.element_to_be_clickable((self.password_field))
        )
        if 'user' in user_name:
            password_field.send_keys(USER_PASSWORD)
        elif 'editor' in user_name:
            password_field.send_keys(EDITOR_PASSWORD)
        elif 'admin' in user_name:
            password_field.send_keys(ADMIN_PASSWORD)
        else:
            assert 1 == 2, 'Unrecognized user name'


    def get_cookie_dict(self):
        saved_cookies = self.driver.get_cookies()
        return saved_cookies


    def set_logged_in_cookies(self, pass_cookies):
        for cookie in pass_cookies:
            self.driver.add_cookie(cookie)


    def get_local_storage(self):
        local_storage = LocalStorage(self.driver)
        self.stored_items = local_storage.items()
        return self.stored_items


    def set_local_storage(self, stored_items):
        local_storage = LocalStorage(self.driver)
        for key, value in stored_items.items():
            local_storage.set(key, value)


def is_not_chromedriver():
    if DRIVER.lower() != 'authenticated_chrome' and \
        DRIVER.lower() != 'chrome' and \
        DRIVER.lower() != 'custom_device' and \
        DRIVER.lower() != 'headless_chrome' and \
        DRIVER.lower() != 'remote_chrome' and \
        DRIVER.lower() != 'remote_authenticated_chrome' and \
        DRIVER.lower() != 'last_headless_chrome':
        return True
    else:
        return False


def firebase_login(user_name):
    '''Get login cookies from firebase using
    https://firebase.google.com/docs/reference/rest/auth/#section-sign-in-email-password'''
    payload =  {
        'email': ACCOUNTS[user_name]['email'],
        'password': ACCOUNTS[user_name]['password'],
        'returnSecureToken': True
    }
    payload = json.dumps(payload)
    firebase_login = 'https://www.googleapis.com/identitytoolkit/v3/' \
        'relyingparty/verifyPassword?key=%s' % FIREBASE_KEY
    r = requests.post(
        firebase_login,
        headers={'Content-Type': 'application/json'},
        data=payload
    )
    assert r.status_code is requests.codes.ok, 'Firebase login returned %d. ' \
        'with message:\n%s' % (r.status_code, r.text)
    return r.json()


def set_firebase_cookies(driver, pass_json):
    driver.add_cookie({
        'name': 'firebaseToken',
        'value': str(pass_json['idToken']),
        'domain': HOST
    })
    driver.add_cookie({
        'name': 'firebaseRefreshToken',
        'value': str(pass_json['refreshToken']),
        'domain': HOST
    })


def delete_firebase_cookies(driver):
    driver.delete_cookie('firebaseToken')
    driver.delete_cookie('firebaseRefreshToken')


def before_all(context):
    code, context.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
    assert code == 200, 'Did not get 200 creating bearer token: %d' % (
        code
    )
    # Add Bearer headers to browsermob proxy
    context.proxy, context.server = get_proxy_and_server(context.bearer_header)
    #
    # If the environment is password protected you may have to login first.
    # This would be a manual login
    # context.browser = Browser()
    # context.driver = context.browser.get_browser_driver()
    # context.driver.get(HOST_URL)
    # context.wait = WebDriverWait(context.driver, 20, 0.25)
    # context.login = SiteLogin(context.driver)
    # context.login.click_login_button()
    # context.login.type_email('user')
    # context.login.click_submit()
    # context.login.type_password('user')
    # context.login.click_submit()
    # set_logged_in_before(context.driver)
    # context.wait.until(EC.presence_of_element_located((
    #     By.CSS_SELECTOR,
    #     'article.main__article'
    # )))
    # time.sleep(1)
    # context.logged_in_cookies = context.login.get_cookie_dict()
    # context.stored_items = context.login.get_local_storage()
    # context.driver.quit()


def after_all(context):
    if context.server is not None:
        context.server.stop()


def before_feature(context, feature):
    # set_logged_in_before(context.driver)
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
    elif 'chrome-only' in context.tags:
        if is_not_chromedriver() is True:
            scenario.skip('Skipping test not supported outside chrome')
            return
    elif 'no-safari' in context.tags:
        if 'safari' in DRIVER:
            scenario.skip('Skipping test not supported in safari')
            return
    if 'local-only' in context.tags:
        if 'http://localhost:4444/wd/hub' != SELENIUM:
            scenario.skip('Skipping test, not supported on hub')
            return
    if 'browser' in context.tags:
        context.browser = Browser(proxy=context.proxy)
        context.driver = context.browser.get_browser_driver()
        if 'chrome' in DRIVER:
            scenario.name += ' in %s %s' % (
                context.driver.capabilities['browserName'].capitalize(),
                context.driver.capabilities['version']
            )
        if 'firefox' in DRIVER:
            scenario.name += ' in %s %s' % (
                context.driver.capabilities['browserName'].capitalize(),
                context.driver.capabilities['browserVersion']
            )
        if context.driver is not None:
            context.wait = WebDriverWait(context.driver, 20, 0.25)
            context.driver.get(HOST_URL)
            # context.login = SiteLogin(context.driver)
            response_json = firebase_login('admin')
            set_firebase_cookies(context.driver, response_json)
            set_logged_in_before(context.driver)
            # if 'authenticated_safari' in DRIVER:
            #     context.driver.execute_script(
            #         'CertificateWarningController.visitInsecureWebsiteWithTemporaryBypass();'
            #     )
            # https://github.com/lightbody/browsermob-proxy/raw/master/browsermob-core/src/main/resources/sslSupport/ca-certificate-rsa.cer
            time.sleep(1)
    elif 'requests' in context.tags:
        requester = SetupRequests()
        context.session = requester.setup_session(context.bearer_header)
        print(context.session.headers)

    elif 'validity' in context.tags:
        context.browser = Browser()
        if sys.platform == 'darwin':
            context.driver = context.browser.get_driver_by_name('local_html_validator')
        else:
            context.driver = context.browser.get_driver_by_name('remote_html_validator')
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
        # if 'authenticated_safari' in DRIVER:
        #     self.safari_proxy = SafariProxy(None, None)
        #     self.safari_proxy.off()
