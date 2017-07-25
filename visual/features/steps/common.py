import os
import time
from PIL import Image, ImageDraw
from cStringIO import StringIO
from pathlib import Path
from pdiffer import pdiff, assert_images_similar
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC

REBASE = os.getenv('REBASE', False)

LOGGING_SECTION_LOCATOR = (By.ID, 'logging-setup')


def create_diff_image(page_name, this_runs_image, difference_image):
    errors = 'qa/visual/results/%s.png' % page_name
    print('Output to\n%s' % errors)
    background = Image.open(this_runs_image)
    overlay = Image.open(difference_image)
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")
    new_img = Image.blend(background, overlay, 0.5)
    new_img.save(errors, "PNG")


def get_element_size(element):
    location = element.location
    size = element.size
    return location, size


def full_height_screenshot(wd):
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
    scroll_height = wd.execute_script(js)
    slices = []
    offset = 0
    while offset < scroll_height:
        wd.execute_script("window.scrollTo(0, %s);" % offset)
        time.sleep(0.5)
        img = Image.open(StringIO(wd.get_screenshot_as_png()))
        offset += img.size[1]
        slices.append(img)

        screenshot = Image.new('RGB', (slices[0].size[0], scroll_height))
        offset = 0
        for img in slices:
            screenshot.paste(img, (0, offset))
            offset += img.size[1]
    return screenshot


def crop_screenshot(image, location, size):
    print(image)
    original_image = Image.open(image)
    time.sleep(2)
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    cropped_image = original_image.crop((left, top, right, bottom))
    cropped_image.save(image, "PNG")


@given('I start "{page}" at "{width}" x "{height}"')
def get(context, page, width, height):
    context.driver.set_window_position(0, 0)
    context.driver.set_window_size(height, width)
    context.current_page = '%s_%s_%s' % (page, width, height)


@given('I am on "{uri}"')
def get(context, uri):
    url = BASE_URL + uri
    context.driver.get(url)


@when('I am on "{uri}"')
def get(context, uri):
    url = BASE_URL + uri
    context.driver.get(url)


@when('I create or compare a screenshot')
def check_expect_given(context):
    context.should_assert = False
    if bool(REBASE) is True:
        print('WARN: File does not exist, creating baseline image at qa/visual/images/baselines/%s.png' %
              context.current_page)
        context.driver.save_screenshot(
            'qa/visual/images/baselines/%s.png' % context.current_page)
    else:
        context.should_assert = True
        context.driver.save_screenshot(
            'qa/visual/images/current_run/%s.png' % context.current_page)
        context.current_baseline = 'qa/visual/images/baselines/%s.png' % context.current_page
        context.current_run = 'qa/visual/images/current_run/%s.png' % context.current_page
        # print('Compare:\n%s\nTo:\n%s' %
        #       (context.current_baseline, context.current_run))
        context.output_path = 'qa/visual/images/diff/%s.png' % context.current_page
        context.current_screenshot = pdiff(
            context.current_baseline,
            context.current_run,
            # threshold=.01,
            output=context.output_path
        )


@when('I find the logging setup section')
def find_logging(context):
    context.current_element = context.driver.find_element(
        *LOGGING_SECTION_LOCATOR)


@when('I create or compare a screenshot of an element')
def check_expect_element(context):
    context.should_assert = False
    if bool(REBASE) is True:
        print('WARN: File does not exist, creating baseline image at qa/visual/images/baselines/%s.png' %
              context.current_page)
        context.driver.full_screenshot = full_height_screenshot(context.driver)
        screenshot_path = 'qa/visual/images/baselines/%s.png' % context.current_page
        context.driver.full_screenshot.save(
            screenshot_path, "PNG")
        location, size = get_element_size(context.current_element)
        print (location)
        print (size)
        crop_screenshot(screenshot_path, location, size)
    else:
        context.should_assert = True
        context.driver.full_screenshot = full_height_screenshot(context.driver)
        context.current_run = 'qa/visual/images/current_run/%s.png' % context.current_page
        context.driver.full_screenshot.save(
            context.current_run, "PNG")
        location, size = get_element_size(context.current_element)
        print (location)
        print (size)
        crop_screenshot(context.current_run, location, size)
        context.current_baseline = 'qa/visual/images/baselines/%s.png' % context.current_page
        context.output_path = 'qa/visual/images/diff/%s.png' % context.current_page
        context.current_screenshot = pdiff(
            context.current_baseline,
            context.current_run,
            # threshold=.01,
            output=context.output_path
        )


@then('it should match')
def match_if_assert_is_true(context):
    # print(bool(context.current_screenshot))
    if context.should_assert is True:
        # Creating difference image
        if bool(context.current_screenshot) is True:
            create_diff_image(
                context.current_page,
                context.current_run,
                context.output_path
            )
        # Failing test if images differ
        assert bool(context.current_screenshot) is False, \
            'Images Differ. Results written to:\nqa/visual/results/%s.png' % (
                context.current_page
        )
    else:
        assert 1 == 2
        print ("Baselines set")
