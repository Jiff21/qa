import time
from behave import given, when, then, step
from qa.environment_variables import ADMIN_URL_DICT
from qa.environment_variables import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NAME
from qa.environment_variables import EDITOR_EMAIL, EDITOR_PASSWORD, EDITOR_NAME
from qa.environment_variables import USER_EMAIL, USER_PASSWORD, USER_NAME
from qa.environment_variables import RECOVERY_EMAIL
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.button')
SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1')
WAIT_FOR_OAUTH_VALUE = (By.CSS_SELECTOR, 'h1')

# No account
EMAIL_ONLY_EMAIL_FIELD = (By.CSS_SELECTOR, 'input#identifierId')
EMAIL_ONLY_EXCLUSIVE_VALUE = (By.CSS_SELECTOR, 'input#identifierId')
EMAIL_ONLY_NEXT_BUTTON = (By.ID, 'identifierNext')
# No account and password only.
GAIA_PASSWORD_FIELD = (By.NAME, 'password')
GAIA_PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
GAIA_SIGN_IN_BUTTONIN_BUTTON = (By.ID, 'passwordNext')
# Multi FLow Values
GAIA_ADD_ACCOUNT_BUTTTON = (By.ID, 'identifierLink')
MULTI_DETECTOR = (By.CSS_SELECTOR, 'div[data-profileindex="0"]')
# For Beyond CMS Product would like to: screen.
AUTH_APP_FOR_USE_DETECTOR = (By.ID, 'third_party_info_container')
AUTH_APP_FOR_USE_DETECTOR_ALLOW_BUTTON = (
    By.CSS_SELECTOR, 'button#submit_approve_access')
LOGIN_PAGE_TITLE = 'Gmail'
DASHBOARD_PAGE_TITLE = 'Inbox'
LOGGED_IN_USER_NAME = (By.CSS_SELECTOR, '#account-settings > em')
CHECK_FAILED_PASSWORD = 'Wrong password. Try again.'
RECOVERY_EMAIL_OPT_LOCATOR = (
    By.XPATH, '//div[contains(text(), "Confirm your recovery email")]')
HEADING_TEXT = (By.ID, 'headingText')
RECOVERY_EMAIL_FIELD = (By.ID, 'knowledge-preregistered-email-response')
GENERIC_NEXT_BUTTON = (By.ID, 'next')


class LoginPage():

    def __init__(self, driver):
        print ('loaded accounts')
        self.driver = driver
        # self.admin_url = ADMIN_URL_DICT[BASE_URL]

    def wait_for_oauth(self):
        print('waiting for oauth.')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(
            ((EMAIL_ONLY_EXCLUSIVE_VALUE))))

    def get_username(self):
        self.username = self.driver.find_element(
            *LOGGED_IN_USER_NAME)
        return self.username.text

    def check_for_login_account(self, ema):
        self.constructed_locator = 'account-' + ema
        self.presence_of_account = len(
            self.driver.find_elements(By.ID, self.constructed_locator))
        return self.presence_of_account

    def get_account_panel(self, ema):
        self.constructed_locator = 'p[' + ema + ']'
        self.current_account = self.driver.find_element(
            By.ID, self.constructed_locator)
        return self.current_account

    def check_for_multi(self):
        self.multi_account_appeared = len(
            self.driver.find_elements(*MULTI_DETECTOR))
        print('in check for multi ' + str(self.multi_account_appeared))
        return bool(self.multi_account_appeared >= 1)

    def check_for_no_account(self):
        time.sleep(2)
        self.email_field_appeared = len(self.driver.find_elements(
            *EMAIL_ONLY_EXCLUSIVE_VALUE))
        print('in check for no account '
              + str(bool(self.email_field_appeared >= 1)))
        return bool(self.email_field_appeared >= 1)

    def check_for_auth_and_accept(self):
        self.multi_account_appeared = len(self.driver.find_elements(
            *AUTH_APP_FOR_USE_DETECTOR))
        if self.multi_account_appeared >= 1:
            print('Had to authorize account use.')
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(
                (AUTH_APP_FOR_USE_DETECTOR_ALLOW_BUTTON)))
            self.allow_button = self.driver.find_element(
                *AUTH_APP_FOR_USE_DETECTOR_ALLOW_BUTTON)
            self.allow_button.click()
        else:
            print('Account already authorized')

    def check_for_verify_its_you(self):
        verify_message = self.driver.find_elements(*HEADING_TEXT)
        if verify_message > 0:
            print('No IP Address Google wants to Verify it\'s you')
            self.verify_by_email = self.driver.find_element(
                *RECOVERY_EMAIL_OPT_LOCATOR)
            self.verify_by_email.click()
            self.email_field = self.driver.find_element(
                *RECOVERY_EMAIL_FIELD)
            self.email_field.send_keys(RECOVERY_EMAIL)
            self.recovery_next_button = self.driver.find_element(
                *GENERIC_NEXT_BUTTON)
            self.recovery_next_button.click()
        else:
            print('No verify challenge')

    def check_success(self, message):
        self.check_for_verify_its_you()
        if CHECK_FAILED_PASSWORD not in self.driver.page_source:
            print ('Logged In! %s' % message)
        else:
            print('I ended up at title %s' % self.driver.title)
            # print 'At EXTRA LARGE SLEEP in check_success/ qa/functional/pages/login_page'
            # time.sleep(10)
            assert 1 is 2, "UNEXPECTED SCENARIO: Got to else in check_success"

    def oauth_email_only(self, ema, pas):
        print('oauth_email_only flow')
        self.email_field = self.driver.find_element(
            *EMAIL_ONLY_EMAIL_FIELD)
        self.email_field.send_keys(ema)
        self.next_button = self.driver.find_element(
            *EMAIL_ONLY_NEXT_BUTTON)
        self.next_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(
            (GAIA_SIGN_IN_BUTTONIN_BUTTON)))
        self.password_field = self.driver.find_element(
            *GAIA_PASSWORD_FIELD)
        self.password_field.send_keys(pas)
        self.sign_in_button = self.driver.find_element(
            *GAIA_SIGN_IN_BUTTONIN_BUTTON)
        self.sign_in_button.click()

    def single_account_no_password(self, pas):
        print('single_account_no_password flow')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(
            (GAIA_SIGN_IN_BUTTONIN_BUTTON)))
        self.password_field = self.driver.find_element(
            *GAIA_PASSWORD_FIELD)
        self.password_field.send_keys(pas)
        self.sign_in_button = self.driver.find_element(
            *GAIA_SIGN_IN_BUTTONIN_BUTTON)
        self.sign_in_button.click()

    def oauth_logic(self, email_account, password_account, name_of_account):
        # Might have to add a wait
        print('In Logic')
        if self.driver.title == DASHBOARD_PAGE_TITLE:
            print('Single Log In still enabled. Logged in.')
        elif LoginPage.check_for_multi(self) is True:
            print('Logic says multi:')
            if LoginPage.check_for_login_account(self, email_account) >= 1:
                print('Found this users Log In card.')
                self.account_to_click = LoginPage.get_account_panel(
                    self, email_account)
                self.account_to_click.click()
                LoginPage.check_for_auth_and_accept(self)
                LoginPage.check_success(self, 'Multi with card.')
            else:
                print('But the user account needs to be added')
                self.add_account_button = self.driver.find_element(
                    *GAIA_ADD_ACCOUNT_BUTTTON)
                self.add_account_button.click()
                time.sleep(2)
                LoginPage.oauth_email_only(
                    self, email_account, password_account)
                LoginPage.check_for_auth_and_accept(self)
                LoginPage.check_success(self, 'Multi but new email')
        elif LoginPage.check_for_no_account(self) is True:
            print('Logic says email only')
            LoginPage.oauth_email_only(self, email_account, password_account)
            LoginPage.check_for_auth_and_accept(self)
            LoginPage.check_success(self, 'Email Only')
        elif self.driver.find_element(
                *GAIA_PASSWORD_FIELD).is_displayed() is True:
            print('Logic says single email, no password')
            LoginPage.single_account_no_password(self, password_account)
            LoginPage.check_for_auth_and_accept(self)
            LoginPage.check_success(self, "Single Email, No Pass")
        else:
            assert 1 is 2, "UNEXPECTED SCENARIO: Got to else in oauth_logic"

    def auto_login_workaround(self, account_in_use, pass_in_use, name_in_use):
        print('AUTO LOGIN WORKAROUND. :::  %s' % self.driver.title)
        if DASHBOARD_PAGE_TITLE in self.driver.title:
            print('Auto logged in. This should be a fail if CMS-86 is fixed')
        elif self.driver.title == LOGIN_PAGE_TITLE:
            LoginPage.oauth_logic(self, account_in_use,
                                  pass_in_use, name_in_use)
        elif self.driver.title == 'Sign in - Google Accounts':
            assert 1 == 2, \
                "UNEXPECTED SCENARIO: Still on Google OAUTH in test_page_title"
        else:
            time.sleep(10)
            assert 1 == 2, "UNEXPECTED SCENARIO: Got to else in test_page_title"


@step('I log into google using as "{name}"')
def login(context, name):
    context.user_name = name.lower()
    email = ACCOUNTS[context.user_name]['email']
    password = ACCOUNTS[context.user_name]['password']
    login = LoginPage(context.driver)
    login.auto_login_workaround(email, password, name)
