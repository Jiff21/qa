import os
from PIL import Image, ImageDraw
from pathlib import Path
from pdiffer import pdiff, assert_images_similar
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC

REBASE = os.getenv('REBASE', False)


def create_diff_image(page_name, this_runs_image, difference_image):
    errors = 'qa/visual/results/%s.png' % page_name
    print('Output to\n%s' % errors)
    background = Image.open(this_runs_image)
    overlay = Image.open(difference_image)
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")
    new_img = Image.blend(background, overlay, 0.5)
    new_img.save(errors, "PNG")


@given('I start "{page}" at "{width}" x "{height}"')
def get(context, page, width, height):
    context.driver.set_window_position(0, 0)
    context.driver.set_window_size(height, width)
    context.current_page = '%s_%s_%s' % (page, width, height)


@given('I am on "{uri}"')
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


@then('it should match')
def check_expect_when(context):
    print(bool(context.current_screenshot))
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
