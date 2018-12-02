import time
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from qa.settings import HOST_URL, PAGES_DICT
from qa.settings import USER_EMAIL, USER_PASSWORD


@step('I hit the tab key "{number:d}" time(s)')
def step_impl(context, number):
    i = 0
    while i < number:
        action = ActionChains(context.driver)
        action.send_keys(Keys.TAB).perform();
        i += 1
    context.current_element = context.driver.switch_to.active_element


@step('I send the user email to the current element')
def step_impl(context):
    context.current_element.send_keys(USER_EMAIL)


@step('I send the user password to the current element')
def step_impl(context):
    context.current_element.send_keys(USER_PASSWORD)


@step('I click the current element')
def step_impl(context):
    context.current_element.click()


@step('the current element alt field should include "{word}"')
def step_impl(context, word):
    assert word in context.current_element.text, "Did not see %s in text:\n%s" % (
        word,
        context.current_element.text
    )
