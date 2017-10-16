from behave import given, when, then
import time

@then('the header should be exactly "{words}"')
def find_header(context, words):
    el = context.driver.find_element(*HEADER_PATH)
    assert_that(el.text, equal_to(words))
