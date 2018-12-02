import requests
from behave import given, when, then, step
from qa.settings import HOST_URL, PAGES_DICT

@step('I call the api "{page_name}"')
def step_impl(context, page_name):
    context.current_url = HOST_URL + PAGES_DICT[page_name]
    context.response = requests.get(context.current_url)

@step('I get the browser url')
def get(context):
    context.browser_url = context.driver.current_url

@step('I try to go to http version of "{page_name}"')
def get(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = HOST_URL + PAGES_DICT[context.page_name]
    context.current_url = context.current_url.replace('https', 'http')
    print('On this url %s' % context.current_url)
    context.driver.get(context.current_url)

@step('it should contain https')
def get(context):
    assert 'https' in context.browser_url, 'Did not upgrade http request to ' \
        'https.'

@step('I find the "{header_name}" header')
def step_impl(context, header_name):
    try:
        context.current_header = context.response.headers[header_name]
    except:
        assert True == False, 'Header not found in response'

@step('it should have the X-Content-Type-Options set to no-sniff')
def step_impl(context):
    assert 'nosniff' in context.current_header, 'Did not find no sniff, ' \
        'instead %s' % context.current_header

@step('it should have the X-Frame-Options set to SAMEORIGIN')
def step_impl(context):
    assert 'SAMEORIGIN' in context.current_header, 'Did not find SAMEORIGIN, ' \
        'instead %s' % context.current_header

@step('it should have the X-XSS-Protection set to 1')
def step_impl(context):
    assert '1' in context.current_header, 'Did not find 1, instead %s' \
        % (context.current_header)

@step('the CSP should contain "{csp_item}"')
def step_impl(context, csp_item):
    assert csp_item in context.current_header, 'Did not find %s, instead %s' \
        % (csp_item, context.current_header)

@step('I get all cookies')
def step_impl(context):
    context.cookies = context.driver.get_cookies()
    # for cookie in context.cookies:
    #     print(cookie)

@step('the ones from our domain should be secure')
def step_impl(context):
    cookie_errors = []
    for cookie in context.cookies:
        if cookie['domain'][1:] in HOST_URL:
            if cookie['name'] == '_gid' or '_gat' in cookie['name'] \
                or cookie['name'] == '_ga':
                continue
            else:
                try:
                    assert cookie['secure'] == True
                except:
                    string = '%s cookie is not marked secure.' % (
                        cookie['name']
                    )
                    cookie_errors.append(string)
    assert len(cookie_errors) == 0, loop_thru_messages(cookie_errors)

@step('I add "{data_attack}" to the URL')
def step_impl(context, data_attack):
    context.current_url = HOST_URL + PAGES_DICT['index'] + data_attack
    context.response = requests.get(context.current_url)

@step('the response is a "{expected_status:d}"')
def step_impl(context, expected_status):
    assert context.response.status_code == expected_status, 'Expected a %d ' \
        'for %s.' % (
            expected_status,
            context.current_url,
        )
