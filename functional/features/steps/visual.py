from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


def get_element_corner_locations(element):
    '''
    returns the coordinates of the corners of an element in a dictionary
    '''
    # print('text %s' % element.text)
    current_element_width = element.size['width']
    # print('current_element_width %d' % current_element_width)
    current_element_height = element.size['height']
    # print('current_element_height %d' % current_element_height)
    # print('location %s' % element.location)
    element_corners = {
        'top left': element.location,
        'top right': {
            'x': element.location['x'] + current_element_width,
            'y': element.location['y']
        },
        'bottom left': {
            'x': element.location['x'],
            'y': element.location['y'] + current_element_height
        },
        'bottom right': {
            'x': element.location['x'] + current_element_width,
            'y': element.location['y'] + current_element_height
        }
    }
    return element_corners


def calc_distance_above(above_element, below_element):
    '''
    returns the distance of an element based on location
    '''
    above_corners = get_element_corner_locations(above_element)
    below_element = get_element_corner_locations(above_element)
    return below_element['bottom left'] - above_corners['bottom left']


@step(
    'the current element should be "{least_less_equal}" "{expected_size:d}"px '\
    'above the comparison element'
)
def step_impl(context, least_less_equal, expected_size):
    context.current_element_corners = get_element_corner_locations(
        context.current_element
    )
    context.comparison_element_corners = get_element_corner_locations(
        context.comparison_element
    )
    context.current_above_comparison_distance = int(
        context.comparison_element_corners['top left']['y']
    ) - int(
        context.current_element_corners['bottom left']['y']
    )
    if 'least' in least_less_equal.lower():
        assert context.current_above_comparison_distance > expected_size, \
            'Expected it to be at least %ipx from comparison object instead ' \
            'got %i' % (
                expected_size,
                context.current_above_comparison_distance
            )
    elif 'less' in least_less_equal.lower():
        assert context.current_above_comparison_distance < expected_size, \
            'Expected it to be less than %ipx from comparison object instead ' \
            'got %i' % (
                expected_size,
                context.current_above_comparison_distance
            )
    elif 'equal' in least_less_equal.lower():
        assert context.current_above_comparison_distance == expected_size, \
            'Expected it to be equal to %i instead got %i' % (
                expected_size,
                context.current_above_comparison_distance
            )
    else:
        assert False, 'Unexpected value for more_less_equal,' \
            ' got: %s' % least_less_equal



@step(
    'the current element should be horizontally "{left_right}" aligned with '\
    'the comparison element'
)
def step_impl(context, left_right):
    left_right = left_right.lower()
    assert left_right == 'left' or left_right == 'right', "Got unexpected "\
    "value, expect either 'left' or 'right'."
    context.current_element_corners = get_element_corner_locations(
        context.current_element
    )
    context.comparison_element_corners = get_element_corner_locations(
        context.comparison_element
    )
    locator = 'top %s' % left_right
    assert round(context.current_element_corners[locator]['x']) == \
        round(context.comparison_element_corners[locator]['x']), \
        "Expcted both to have same y position, current is here %s & " \
        "comparison element is %s." % (
            round(context.current_element_corners[locator]['x']),
            round(context.comparison_element_corners[locator]['x'])
        )


@step(
    'the current element should be vertically "{top_bottom}" aligned with the '\
    'comparison element'
)
def step_impl(context, top_bottom):
    top_bottom = top_bottom.lower()
    assert top_bottom == 'top' or top_bottom == 'bottom', "Got unexpected " \
        "value, expect either 'top' or 'bottom'."
    context.current_element_corners = get_element_corner_locations(
        context.current_element
    )
    context.comparison_element_corners = get_element_corner_locations(
        context.comparison_element
    )
    locator =  '%s left' % top_bottom
    assert round(context.current_element_corners[locator]['y']) == \
        round(context.comparison_element_corners[locator]['y']), \
        "Expcted both to have same y position, current is here %s & " \
        "comparison element is %s." % (
            round(context.current_element_corners[locator]['y']),
            round(context.comparison_element_corners[locator]['y'])
        )


@step(
    'the current element should have "{expected_size:d}"px padding on all sides'
)
def step_impl(context, expected_size):
    # This has to be done individually for firefox.
    # https://github.com/mozilla/geckodriver/issues/1130#issuecomment-357948268
    assert expected_size == context.current_element.value_of_css_property(
        'padding-top'
    ), 'expected %d padding-top but got %s.' % (
        expected_size,
        context.current_element.value_of_css_property('padding-top')
    )
    assert expected_size == context.current_element.get_attribute(
        'padding-bottom'
    ), 'expected %d padding-bottom but got %d.' % (
        expected_size,
        context.current_element.value_of_css_property('padding-bottom')
    )
    assert expected_size == context.current_element.get_attribute(
        'padding-left'
    ), 'expected %d padding-left but got %d.' % (
        expected_size,
        context.current_element.value_of_css_property('padding-left')
    )
    assert expected_size == context.current_element.value_of_css_property(
        'padding-right'
    ), 'expected %d padding-right but got %d.' % (
        expected_size,
        context.current_element.value_of_css_property('padding-right')
    )


def checklower(current, compare, corner, x_or_y):
    assert round(current[corner][x_or_y]) < round(compare[corner][x_or_y]), \
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
    assert round(current[corner][x_or_y]) > round(compare[corner][x_or_y]), \
        'expected current element %s %s (%d) to be more than comparison ' \
        'element %s %s (%d).' % (
            corner,
            x_or_y,
            round(current[corner][x_or_y]),
            corner,
            x_or_y,
            round(compare[corner][x_or_y])
        )



@step(
    'the current element should be "{inside_or_outside}" the comparison element'
)
def step_impl(context, inside_or_outside):
    inside_or_outside = inside_or_outside.lower()
    assert inside_or_outside == 'inside' or inside_or_outside == 'outside', \
        "Got unexpected value, expected either 'inside' or 'outside'."
    context.current_element_corners = get_element_corner_locations(
        context.current_element
    )
    # print('\n')
    # print('current el %s' % context.current_element.text)
    # print('current x %d' % context.current_element_corners['top left']['x'])
    context.comparison_element_corners = get_element_corner_locations(
        context.comparison_element
    )
    # print('compare el %s' % context.comparison_element.text)
    # print('compare x %d' % context.comparison_element_corners['top left']['x'])
    # print('\n')
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
    assert context.current_element_width <= window_size['width'], 'Expected ' \
        'current element width (%d) to be less than or equal to window width ' \
        '(%d)' % (
            context.current_element_width,
            window_size['width']
        )
