'''
Feature: Google your way to documentation

  Scenario: Google
    Given I am on google.com
    When  I type in "Behave Python"
        and I hit return
    Then  The results should contain "Behave"

'''
from behave   import given, when, then
from hamcrest import assert_that, equal_to
from google_object import Google

@given('I am on "{url}"')
def get(context, url):
    context.google = Google()
    context.google.get(url)

@when('II put "{thing}" in a blender')
def step_when_switch_blender_on(context, thing):
    context.blender.switch_on()

@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    assert_that(context.blender.result, equal_to(other_thing))
