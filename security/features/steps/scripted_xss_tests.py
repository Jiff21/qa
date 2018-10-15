import os
import json
import re
import sys
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.settings import QA_FOLDER_PATH

SEARCH_FIELD_LOCATOR = (By.NAME, 's')


@when('I set current element to search field')
def step_impl(context):
    context.current_element = context.driver.find_element(
        *SEARCH_FIELD_LOCATOR)
    context.current_element.click()


@when('I send the attack "{attack}"')
def step_impl(context, attack):
    context.current_element.clear()
    context.current_element.send_keys(attack)
    context.current_element.send_keys(Keys.RETURN)


@then('there should not be an element with this locator "{css_locator}"')
def step_impl(context, css_locator):
    context.driver.find_elements(By.CSS_SELECTOR, css_locator)
