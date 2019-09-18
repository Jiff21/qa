
import os
import time
from PIL import Image
from PIL import ImageChops
from io import StringIO
from io import BytesIO
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

REBASE = os.getenv('REBASE', False)

LOGGING_SECTION_LOCATOR = (By.ID, 'logging-setup')


def os_path(file_name, path):
    current_directory = os.path.dirname(__file__)
    relative_path = path + file_name + '.png'
    destination = os.path.join(current_directory, relative_path)
    return destination


def check_for_diff(baseline, this_runs_image, output_diff):
    """
    Compares two images and saves a diff image, if there
    is a difference

    @param: path_one: The path to the first image
    @param: path_two: The path to the second image
    """
    image_one = Image.open(baseline)
    image_two = Image.open(this_runs_image)

    diff = ImageChops.difference(image_one, image_two)
    print(diff)

    if diff.getbbox():
        diff.save(output_diff)

    return diff



def create_diff_image(page_name, this_runs_image, difference_image):
    errors = os_path(page_name, '../../images/diffs/')
    print('Differences images written to:\n%s' % errors)
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


def disable_nav(driver):
    js = 'document.getElementById("global-header")'\
        '.setAttribute("style", "position: absolute; top: 0px;"); '\
        'mobileNav = document.getElementById("global-nav-mobile-trigger"); '\
        'mobileNav.parentElement.setAttribute("style", "position: absolute; top: 0px;");'
    print('\n\n%s\n\n' % js)
    driver.execute_script(
        js
    )

def full_height_screenshot(driver):
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
    scroll_height = driver.execute_script(js)
    print('Height of page is %d' % scroll_height)
    inner_height = driver.execute_script('return window.innerHeight')
    print('Height of window is %d' % inner_height)
    slices = []
    offset = 0
    while offset < scroll_height + inner_height:
        print('scrolling to %d' % offset)
        driver.execute_script('window.scrollTo(0, %s);' % offset)
        time.sleep(0.5)
        img = Image.open(BytesIO(driver.get_screenshot_as_png()))
        # Think about disabling nav the nav if it's sticky
        # if offset == 0:
        #     disable_nav(driver)
        slices.append(img)
        screenshot = Image.new('RGB', (slices[0].size[0], scroll_height))
        offset += inner_height
        # offset += img.size[1]
    main_offset = 0
    for img in slices:
        screenshot.paste(img, (0, main_offset))
        main_offset += img.size[1]
    return screenshot


def crop_screenshot(image, location, size):
    original_image = Image.open(image)
    time.sleep(2)
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    cropped_image = original_image.crop((left, top, right, bottom))
    cropped_image.save(image, "PNG")


@given('I start "{page}" at "{width}" x "{height}"')
def name_and_size(context, page, width, height):
    context.driver.set_window_position(0, 0)
    context.driver.set_window_size(width, height)
    page = page.replace(' ', '-').lower()
    browser = context.driver.capabilities['browserName'].lower()
    context.current_page = '%s_%s_%s_%s' % (page, width, height, browser)
    time.sleep(2)


@when('I find the logging setup section')
def find_logging(context):
    context.current_element = context.driver.find_element(
        *LOGGING_SECTION_LOCATOR)


@when('I create or compare a screenshot')
def check_expect_given(context):
    context.should_assert = False
    if bool(REBASE) is True:
        print(
            'WARN: File does not exist, creating baseline image at ' \
            'qa/functional/images/baselines/%s.png' % context.current_page
        )
        context.current_path = os_path(
            context.current_page,
            '../../images/baselines/'
        )
        # context.driver.save_screenshot(context.current_path)
        context.driver.full_screenshot = full_height_screenshot(context.driver)
        context.driver.full_screenshot.save(
            context.current_path,
            "PNG"
        )
    else:
        context.should_assert = True
        context.current_baseline = os_path(
            context.current_page,
            '../../images/baselines/'
        )
        context.current_run = os_path(
            context.current_page,
            '../../images/current_run/'
        )
        context.driver.save_screenshot(context.current_run)
        context.driver.full_screenshot = full_height_screenshot(context.driver)
        context.driver.full_screenshot.save(
            context.current_run
        )

        # print('Compare:\n%s\nTo:\n%s' %
        #       (context.current_baseline, context.current_run))
        context.output_path = os_path(
            context.current_page,
            '../../images/diffs/'
        )
        context.current_screenshot = check_for_diff(
            context.current_baseline,
            context.current_run,
            context.output_path
        )



@when('I create or compare a screenshot of an element')
def check_expect_element(context):
    context.should_assert = False
    if bool(REBASE) is True:
        context.screenshot_path = os_path(
            context.current_page, '../../images/baselines/')
        print(
            'WARN: File does not exist, creating baseline element image at %s' %
             context.screenshot_path
        )
        context.driver.full_screenshot = full_height_screenshot(context.driver)
        context.driver.full_screenshot.save(
            context.screenshot_path,
            "PNG"
        )
        location, size = get_element_size(context.current_element)
        # print (location)
        # print (size)
        crop_screenshot(context.screenshot_path, location, size)
    else:
        context.should_assert = True
        context.current_baseline = os_path(
            context.current_page,
            '../../images/baselines/'
        )
        context.current_run = os_path(
            context.current_page,
            '../../images/current_run/'
        )
        print(context.current_run)
        context.driver.save_screenshot(context.current_run)
        context.driver.full_screenshot = full_height_screenshot(context.driver)
        context.driver.full_screenshot.save(
            context.current_run, "PNG")
        location, size = get_element_size(context.current_element)
        crop_screenshot(context.current_run, location, size)

        print("comparing")

        context.output_path = os_path(
            context.current_page, '../../images/diffs/')
        context.current_screenshot = check_for_diff(
            context.current_baseline,
            context.current_run,
            context.output_path
        )


@then('it should match')
def match_if_assert_is_true(context):
    if bool(REBASE) is False:
        assert context.current_screenshot is False, "Image has changed see file at %s" % (
            context.output_path
        )
    else:
        assert 1 == 2,  'Baselines set'
