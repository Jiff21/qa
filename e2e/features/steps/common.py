from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from qa.environment_variables import BASE_URL


@given('I am on "{uri}"')
def get(context, uri):
    context.current_url = ''
    if uri.lower() == 'index':
        context.current_url = BASE_URL
    else:
        context.current_url = BASE_URL + uri
    context.driver.get(context.current_url)
