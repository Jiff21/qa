import re
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from qa.settings import log

def get_element_corner_locations(self, element):
    '''
    returns the coordinates of the corners of an element in a dictionary
    '''
    # current_element_width = element.size['width']
    # current_element_height = element.size['height']
    # element_corners = {
    #     'top left': element.location,
    #     'top right': {
    #         'x': element.location['x'] + current_element_width,
    #         'y': element.location['y']
    #     },
    #     'bottom left': {
    #         'x': element.location['x'],
    #         'y': element.location['y'] + current_element_height
    #     },
    #     'bottom right': {
    #         'x': element.location['x'] + current_element_width,
    #         'y': element.location['y'] + current_element_height
    #     }
    # }
    # return element_corners
    # Javascript seems to deliver more accurate locations
    script = '''
        return arguments[0].getBoundingClientRect()
    '''
    box = self.driver.execute_script(script, element)
    scrolled_right = self.driver.execute_script('return window.pageXOffset')
    scrolled_down = self.driver.execute_script('return window.pageYOffset')
    element_corners = {
        'top left':  {
            'x': box['left'] + scrolled_right,
            'y': box['top'] + scrolled_down
        },
        'top right': {
            'x': box['right'] + scrolled_right,
            'y': box['top'] + scrolled_down
        },
        'bottom left': {
            'x': box['left'] + scrolled_right,
            'y': box['bottom'] + scrolled_down
        },
        'bottom right': {
            'x': box['right'] + scrolled_right,
            'y': box['bottom'] + scrolled_down
        },
        'center' : {
            'x': (box['left'] + (box['width'] / 2) ) + scrolled_right,
            'y': (box['top'] + (box['height'] / 2) ) + scrolled_down
        }
    }
    return element_corners

def calc_distance_above(self, above_element, below_element):
    '''
    returns the distance between the above element and the below element
    '''
    above_corners = get_element_corner_locations(self, above_element)
    below_element = get_element_corner_locations(self, below_element)
    return round(below_element['top left']['y'] - above_corners['bottom left']['y'])


def distance_asserts(type, value, expected):
    if 'maximum' in type.lower():
        assert value <= expected, \
            'Expected it to be a maximum of %i px from comparison object instead ' \
            'got %i px' % (
                expected,
                value
            )
    elif 'less' in type.lower():
        assert value < expected, \
            'Expected it to be less than %i px from comparison object instead ' \
            'got %i px' % (
                expected,
                value
            )
    elif 'equal' in type.lower():
        assert value == expected, \
            'Expected it to be equal to %i px instead got %i px' % (
                expected,
                value
            )
    elif 'more' in type.lower():
        assert value > expected, \
            'Expected it to be at least %i px from comparison object instead ' \
            'got %i px' % (
                expected,
                value
            )
    elif 'least' in type.lower():
        assert value >= expected, \
            'Expected it to be at least %i px from comparison object instead ' \
            'got %i px' % (
                expected,
                value
            )
    else:
        assert False, 'Unexpected value for type of comparison,' \
            ' got: %s' % type



@step('the current element should be "{least_less_equal}" "{expected_size:d}"px above the comparison element')
def step_impl(context, least_less_equal, expected_size):
    context.current_above_comparison_distance = calc_distance_above(context, context.current_element, context.comparison_element)
    log.debug('above comparison')
    distance_asserts(least_less_equal, context.current_above_comparison_distance, expected_size)


def calc_distance_right(self, left_el, right_el):
    '''
    returns the distance between the left element and the right element
    '''
    left_el_corners = get_element_corner_locations(self, left_el)
    right_el_corners = get_element_corner_locations(self, right_el)
    return round(right_el_corners['top left']['x'] - left_el_corners['top right']['x'])


@step('the current element should be "{least_less_equal}" "{expected_size:d}"px to the right the comparison element')
def step_impl(context, least_less_equal, expected_size):
    context.right_of_dist = calc_distance_right(context, context.comparison_element, context.current_element)
    log.debug('to the right comparison')
    distance_asserts(least_less_equal, context.right_of_dist, expected_size)


@step('the current element should be "{least_less_equal}" "{expected_size:d}"px inside from the "{side}" of the comparison element')
def step_impl(context, least_less_equal, expected_size, side):
    context.current_element_corners = get_element_corner_locations(context, context.current_element)
    context.comparison_element_corners = get_element_corner_locations(context, context.comparison_element)
    if side == 'top':
        context.inside_dist = round(
            context.current_element_corners['top left']['y'] -
            context.comparison_element_corners['top left']['y']
        )
    elif side == 'right':
        context.inside_dist =round(
            context.comparison_element_corners['top right']['x'] -
            context.current_element_corners['top right']['x']
        )
    elif side == 'bottom':
        context.inside_dist = round(
            context.comparison_element_corners['bottom left']['y'] -
            context.current_element_corners['bottom left']['y']
        )
    elif side == 'left':
        context.inside_dist =round(
            context.current_element_corners['top left']['x'] -
            context.comparison_element_corners['top left']['x']
        )
    else:
        assert False, 'Unrecognized side (%s) of comparison element to ' \
            'measure inside from.' % side
    log.debug('to the inside comparison')
    log.debug('inside_dist %s' % str(context.inside_dist))
    log.debug('expected_size %s' % str(expected_size))
    distance_asserts(least_less_equal, context.inside_dist, expected_size)


@step('the current element should be horizontally "{left_right_center}" aligned (+/- {margin_of_error:d}) with the comparison element')
def step_impl(context, left_right_center, margin_of_error):
    left_right_center = left_right_center.lower()
    assert left_right_center == 'left'  \
        or left_right_center == 'right' \
        or left_right_center == 'center', \
        "Got unexpected value, expect either 'left', 'right' or 'center'."
    context.current_element_corners = get_element_corner_locations(context, context.current_element)
    context.comparison_element_corners = get_element_corner_locations(context, context.comparison_element)
    if left_right_center == 'left' or left_right_center == 'right':
        locator = 'top %s' % left_right_center
    else:
        locator = 'center'
    # log.debug('horizontally aligned lrc current element:\n%s\n' % context.current_element.text)
    # log.debug('horizontally aligned lrc comparison element:\n%s\n' % context.comparison_element.text)
    log.debug('horizontally aligned lrc current element corners:\n%s\n' % context.current_element_corners)
    log.debug('horizontally aligned lrc comparison element corners:\n%s\n' % context.comparison_element_corners)
    assert round(context.comparison_element_corners[locator]['x']) - margin_of_error \
        <= round(context.current_element_corners[locator]['x']) \
        <= round(context.comparison_element_corners[locator]['x']) + margin_of_error, \
        "Expected both to have same x position, current elment has %s & " \
        "comparison element has %s." % (
            round(context.current_element_corners[locator]['x']),
            round(context.comparison_element_corners[locator]['x'])
        )


@step('the current element should be vertically "{top_bottom_center}" aligned (+/- {margin_of_error:d}) with the comparison element')
def step_impl(context, top_bottom_center, margin_of_error):
    top_bottom_center = top_bottom_center.lower()
    assert top_bottom_center == 'top' \
        or top_bottom_center == 'bottom' \
        or top_bottom_center == 'center', \
        "Got unexpected value, expect either 'top' or 'bottom'."
    context.current_element_corners = get_element_corner_locations(context, context.current_element)
    context.comparison_element_corners = get_element_corner_locations(context, context.comparison_element)
    if top_bottom_center == 'top' or top_bottom_center == 'bottom':
        locator = '%s left' % top_bottom_center
    else:
        locator = 'center'
    assert round(context.comparison_element_corners[locator]['y']) - margin_of_error \
        <= round(context.current_element_corners[locator]['y']) \
        <= round(context.comparison_element_corners[locator]['y']) + margin_of_error, \
        "Expected both to have same y position, current is here %s & " \
        "comparison element is %s." % (
            round(context.current_element_corners[locator]['y']),
            round(context.comparison_element_corners[locator]['y'])
        )



@step('the current element should have "{expected_size}" padding on all sides')
def step_impl(context, expected_size):
    # This has to be done individually for firefox.
    # https://github.com/mozilla/geckodriver/issues/1130#issuecomment-357948268
    assert expected_size == context.current_element.value_of_css_property('padding-top'), \
        'expected %s padding-top but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('padding-top')
    )
    assert expected_size == context.current_element.value_of_css_property('padding-bottom'), \
        'expected %s padding-bottom but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('padding-bottom')
    )
    assert expected_size == context.current_element.value_of_css_property('padding-left'), \
        'expected %s padding-left but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('padding-left')
    )
    assert expected_size == context.current_element.value_of_css_property('padding-right'), \
        'expected %s padding-right but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('padding-right')
    )


@step('the current element should have "{expected_size}" margin on all sides')
def step_impl(context, expected_size):
    # This has to be done individually for firefox.
    # https://github.com/mozilla/geckodriver/issues/1130#issuecomment-357948268
    assert expected_size == context.current_element.value_of_css_property('margin-top'), \
        'expected %s margin-top but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('margin-top')
    )
    assert expected_size == context.current_element.value_of_css_property('margin-bottom'), \
        'expected %s margin-bottom but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('margin-bottom')
    )
    assert expected_size == context.current_element.value_of_css_property('margin-left'), \
        'expected %s margin-left but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('margin-left')
    )
    assert expected_size == context.current_element.value_of_css_property('margin-right'), \
        'expected %s margin-right but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('margin-right')
    )

@step('the current element should have "{expected_size}" margin "{direction}"')
def step_impl(context, expected_size, direction):
    attribute = 'margin-%s' % direction
    current_size = str(context.current_element.value_of_css_property(attribute))
    assert expected_size == current_size, \
        'expected %s %s but got %s.' % (
            expected_size,
            attribute,
            current_size
        )


@step('the current element should have "{expected_size}" padding "{direction}"')
def step_impl(context, expected_size, direction):
    attribute = 'padding-%s' % direction
    current_size = str(context.current_element.value_of_css_property(attribute))
    assert expected_size == current_size, \
        'expected %s %s but got %s.' % (
            expected_size,
            attribute,
            current_size
        )




@step('the comparison element should have "{expected_size}" padding "{direction}"')
def step_impl(context, expected_size, direction):
    attribute = 'padding-%s' % direction
    current_size = str(context.comparison_element.value_of_css_property(attribute))
    assert expected_size == current_size, \
        'expected %s %s but got %s.' % (
            expected_size,
            attribute,
            current_size
        )


@step('the comparison element should have "{expected_size}" margin "{direction}"')
def step_impl(context, expected_size, direction):
    attribute = 'margin-%s' % direction
    current_size = str(context.comparison_element.value_of_css_property(attribute))
    assert expected_size == current_size, \
        'expected %s %s but got %s.' % (
            expected_size,
            attribute,
            current_size
        )

class WindowSize(object):

    def __init__(self):
        log.info('Instanciating window size')

    def def_get_width(self, d):
        return d.execute_script(
            '''
            html = document.querySelector('html')
            body = document.querySelector('body')
            width =  Math.max(
                body.scrollWidth,
                body.offsetWidth,
                html.clientWidth,
                html.scrollWidth,
                html.offsetWidth
            );
            return width
            '''
        )

    def def_get_height(self, d):
        return d.execute_script(
            '''
            html = document.querySelector('html')
            body = document.querySelector('body')
            height =  Math.max(
                body.scrollHeight,
                body.offsetHeight,
                html.clientHeight,
                html.scrollHeight,
                html.offsetHeight
            );
            return height
            '''
        )

    def get_page_size(self, d):
        width = self.def_get_width(d)
        height = self.def_get_height(d)
        page_sides = {
            'top' : 0,
            'right' : width,
            'bottom' : height,
            'left' : 0
        }
        return page_sides


@step('the "{current_comparison}" element should be "{expected_size:d}"px (+/- {number:d}) from the "{direction}" side of the page')
def step_impl(context, current_comparison, expected_size, number, direction):
    if current_comparison.lower() == 'current':
        corners = get_element_corner_locations(context, context.current_element)
    elif current_comparison.lower() == 'comparison':
        corners = get_element_corner_locations(context, context.comparison_element)
    else:
        assert False, "Unrecognized element to compare."
    window_size = WindowSize()
    page_sides = window_size.get_page_size(context.driver)
    page_location = page_sides[direction]
    if direction.lower() == 'top':
        from_edge = corners['top left']['y']
    elif direction.lower() == 'right':
        element_location = corners['bottom right']['x']
        from_edge = float(page_location) - float(element_location)
    elif direction.lower() == 'bottom':
        element_location = corners['bottom right']['y']
        from_edge = float(page_location) - float(element_location)
    elif direction.lower() == 'left':
        from_edge = corners['top left']['x']
    else:
        assert False, 'Did not recognize direction.'

    assert round(expected_size) - number  \
        <= round(from_edge) \
        <= round(expected_size + number), \
        'expected element to be %d from the edge of the page but it was %d.' % (
        round(expected_size),
        round(from_edge)
    )


def checklower(current, compare, corner, x_or_y):
    assert round(current[corner][x_or_y]) <= round(compare[corner][x_or_y]), \
        'expected current element %s %s (%d) to be less than comparison ' \
        'element %s %s (%d).' % (
            corner,
            x_or_y,
            round(current[corner][x_or_y]),
            corner,
            x_or_y,
            round(compare[corner][x_or_y])
        )


def checkhigher(current, compare, corner, x_or_y):
    assert round(current[corner][x_or_y]) >= round(compare[corner][x_or_y]), \
        'Check Higher expected current element %s %s (%d) to be more than comparison ' \
        'element %s %s (%d).' % (
            corner,
            x_or_y,
            round(current[corner][x_or_y]),
            corner,
            x_or_y,
            round(compare[corner][x_or_y])
        )


@step('the current element should be "{inside_or_outside}" the comparison element')
def step_impl(context, inside_or_outside):
    inside_or_outside = inside_or_outside.lower()
    assert inside_or_outside == 'inside' or inside_or_outside == 'outside', "Got unexpected" \
        "value, expected either 'inside' or 'outside'."
    context.current_element_corners = get_element_corner_locations(context, context.current_element)
    log.debug('inside/outside: current element text:\n%s' % context.current_element.text)
    log.debug('inside/outside: current element corners:\n%s\n' % context.current_element_corners)
    context.comparison_element_corners = get_element_corner_locations(context, context.comparison_element)
    log.debug('inside/outside: comparison element text:\n%s' % context.comparison_element.text)
    log.debug('inside/outside: comparison element coirners:\n%s\n' % context.comparison_element_corners)
    # log.debug('\n')
    if inside_or_outside == 'inside':
        # top left of current element should be further right so higher number
        checkhigher(
            context.current_element_corners,
            context.comparison_element_corners,
            'top left',
            'x'
        )
        # top left of current element should be further up so higher number
        checkhigher(
            context.current_element_corners,
            context.comparison_element_corners,
            'top left',
            'y'
        )
        # top right of current element should be less right so lower number
        checklower(
            context.current_element_corners,
            context.comparison_element_corners,
            'top right',
            'x'
        )
        # top right of current element should be further up so higher number
        checkhigher(
            context.current_element_corners,
            context.comparison_element_corners,
            'top right',
            'y'
        )
        # bottom left of current element should be further right, so higher number
        checkhigher(
            context.current_element_corners,
            context.comparison_element_corners,
            'bottom left',
            'x'
        )
        # bottom left of current element should be higher, so lesser number.
        checklower(
            context.current_element_corners,
            context.comparison_element_corners,
            'bottom left',
            'y'
        )
        # bottom right of current element should be less right, so lesser number.
        checklower(
            context.current_element_corners,
            context.comparison_element_corners,
            'bottom right',
            'x'
        )
        # bottom right of current element should be higher, so lesser number.
        checklower(
            context.current_element_corners,
            context.comparison_element_corners,
            'bottom right',
            'y'
        )
    else:
        checklower(
            context.current_element_corners,
            context.comparison_element_corners,
            'top left',
            'x'
        )
        checklower(
            context.current_element_corners,
            context.comparison_element_corners,
            'top left',
            'y'
        )
        checkhigher(
            context.current_element_corners,
            context.comparison_element_corners,
            'top right',
            'x'
        )
        checklower(
            context.current_element_corners,
            context.comparison_element_corners,
            'top right',
            'y'
        )
        checklower(
            context.current_element_corners,
            context.comparison_element_corners,
            'bottom left',
            'x'
        )
        checkhigher(
            context.current_element_corners,
            context.comparison_element_corners,
            'bottom left',
            'y'
        )
        checkhigher(
            context.current_element_corners,
            context.comparison_element_corners,
            'bottom right',
            'x'
        )
        checkhigher(
            context.current_element_corners,
            context.comparison_element_corners,
            'bottom right',
            'y'
        )


@step('the current element should be less than or equal to window width')
def step_impl(context):
    context.current_element_width = context.current_element.size['width']
    window_size = context.driver.get_window_size()
    log.debug('window size is %s' % window_size)
    log.debug('element width is %s' % context.current_element_width)
    assert context.current_element_width <= window_size['width'], 'Expected current ' \
        'element width (%d) to be less than or equal to window width (%d)' % (
            context.current_element_width,
            window_size['width']
        )

@step('there should be no horizontal scrolling width')
def step_impl(context):
    window_size = context.driver.get_window_size()
    script = 'return document.documentElement.scrollWidth'
    scroll_width = context.driver.execute_script(script)
    assert scroll_width <= window_size['width'], 'Expected scroll width (%d) ' \
        'to be less than or equal to window width (%d)' % (
            scroll_width,
            window_size['width']
        )

@step('the current element should be full bleed (+/- {margin_of_error:d})')
def step_impl(context, margin_of_error):
    context.current_element_width = context.current_element.size['width']
    script = 'return document.documentElement.scrollWidth'
    scroll_width = context.driver.execute_script(script)
    assert round(scroll_width) - margin_of_error \
        <= round(context.current_element_width) \
        <= round(scroll_width) + margin_of_error, \
        "Expected both to have same width, current is %s & " \
        "scroll width is %s." % (
            round(context.current_element_width),
            round(scroll_width)
        )
