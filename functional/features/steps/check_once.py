import re
import requests
from qa.settings import HOST_URL


@step('we get the sitemap')
def step_impl(context):
    context.sitemap_url = HOST_URL + '/sitemap.xml'
    context.response = context.session.get(
        context.sitemap_url,
        allow_redirects=False
    )
    context.sitemap_text = context.response.text
    assert context.response.status_code is requests.codes.ok, \
    ' Unexpectedly got a %d response code' % context.response.status_code


@step('it should include the front end base url')
def step_impl(context):
    assert bool(re.search(HOST_URL, context.sitemap_text)) is True, \
        'Did not find expected url in sitemap, instead sitemap is:\n%s' % (
            context.sitemap_text
        )


@step('it should not contain relative urls')
def step_impl(context):
    assert bool(re.search('<loc>/', context.sitemap_text)) is not True, \
        'Did not get expected url in response, instead:\n %s' % (
            context.sitemap_text
        )


@step('I hit the robots.txt url')
def step_impl(context):
    context.response = context.session.get(HOST_URL + '/robots.txt')


@step('it should have a "{code:d}" status code')
def step_impl(context, code):
    assert context.response.status_code == code, \
    'Did not get %s response, instead %i' % (
        code,
        context.response.status_code
    )


@step('it should contain User-agent: *')
def step_impl(context):
    assert 'User-agent: *' in context.response.text, \
    'Did not find User-agent: * in response.'
