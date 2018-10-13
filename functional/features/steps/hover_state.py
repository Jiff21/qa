import time
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


@step('it should have a background-color of "{color}"')
def step_impl(context, color):
    background = context.current_element.value_of_css_property('background-color')
    assert color in background, "Did not get %s background. Instead %s" % (
        color,
        background
    )


@step('it should have a background-image with "{uri}"')
def step_impl(context, uri):
    background = context.current_element.value_of_css_property('background-image')
    assert uri in background, "Did not get %s background uri. Instead %s" % (
        uri,
        background
    )


@step('it should have a text-decoration of "{value}"')
def step_impl(context, value):
    decoration = context.current_element.value_of_css_property('text-decoration')
    assert value in decoration, "Did not get %s decoration. Instead %s" % (
        value,
        decoration
    )



@step('it should have the alt text "{value}"')
def step_impl(context, value):
    alt_text = context.current_element.get_attribute('alt')
    assert alt_text == value, "Did not get %s alt text. Instead %s" % (
        value,
        alt_text
    )


@step('the image uri should include "{value}"')
def step_impl(context, value):
    image_src = context.current_element.get_attribute('src')
    assert value in image_src, "Did not get %s in image src. Instead %s" % (
        value,
        alt_text
    )


@step('it should have a color of "{color}"')
def step_impl(context, color):
    css_color = context.current_element.value_of_css_property('color')
    assert color in css_color, "Did not get %s color. Instead %s" % (
        color,
        css_color
    )


@step('it should have an outline of "{pixels}"')
def step_impl(context, pixels):
    outline_border = context.current_element.value_of_css_property('outline')
    assert pixels in outline_border, "Did not get %s outline. Instead %s" % (
        pixels,
        outline_border
    )


@step('it should have an underline that is "{color}" color')
def step_impl(context, color):
    underline = context.current_element.value_of_css_property('border-bottom-color')
    assert color in underline, "Did not get %s underline color. Instead %s" % (
        pixels,
        outline_border
    )
