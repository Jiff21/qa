import bs4
import re
import requests
import time
from qa.settings import log
from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from qa.settings import HOST_URL, IAP_ON, PAGES_DICT
from qa.functional.features.steps.workarounds import scroll_to_webelement
from qa.functional.features.steps.custom_exceptions import loop_thru_messages
from qa.functional.features.steps.hover_state import *
from qa.functional.features.steps.seo import SeoChecker

class easy_wait():

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, locator, type="By.CSS_SELECTOR"):
        element = None
        try:
            wait = WebDriverWait(
                self.driver,
                10,
                poll_frequency=1,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException
                ]
            )
            element = wait.until(EC.element_to_be_clickable(
                self.driver.find_element(type, locator)
            ))
        except:
            print('Could not find element with %s using %s' % (
                locator,
                type
            ))
        return element


@step('I am on "{page_name}"')
def get(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = HOST_URL + PAGES_DICT[context.page_name]
    log.info('On this url %s' % context.current_url)
    context.driver.get(context.current_url)


@step('I get "{page_name}" with requests session')
def get_requests(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = HOST_URL + PAGES_DICT[context.page_name]
    log.info('Getting this url with reqests %s' % context.current_url)
    context.response = context.session.get(context.current_url)
    assert context.response.status_code is requests.codes.ok, \
    ' Unexpectedly got a %d response code' % context.response.status_code


@step('it setup the seo checker')
def step_impl(context):
    context.seo = SeoChecker()
    context.seo.get_facebook_og_title(context.response.text)


@step('it should have an og:title')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_facebook_og_title(
        context.response.text
    )


@step('it should have an og:description')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_facebook_og_description(
        context.response.text
    )


@step('it should have an og:image')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_facebook_og_image(
        context.response.text
    )


@step('it should have an og:url')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_facebook_og_url(
        context.response.text
    )


@step('the content attribute should not be empty')
def step_impl(context):
    context.current_meta_tag = context.seo.content_not_empty(
        context.current_meta_tag
    )


@step('it should have a twitter:card meta tag')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_twitter_card_card(
        context.response.text
    )


@step('it should have a twitter:site meta tag')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_twitter_card_site(
        context.response.text
    )



@step('it should have a twitter:image meta tag')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_twitter_card_image(
        context.response.text
    )


@step('it should have a twitter:title meta tag')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_twitter_card_title(
        context.response.text
    )


@step('it should have a twitter:description meta tag')
def step_impl(context):
    context.seo = SeoChecker()
    context.current_meta_tag = context.seo.get_twitter_card_description(
        context.response.text
    )


@step('I get all rel icon links')
def step_impl(context):
    soup = bs4.BeautifulSoup(
        context.response.text,
        features="html.parser"
    )
    context.icon_links = soup.findAll('link', attrs={'rel': re.compile('icon')})


def check_for_rel_icon(content):
    if re.search(u'rel=\"icon\"', content):
        return True

def check_for_rel_shortcut_icon(content):
    if re.search(u'rel=\"shortcut icon\"', content):
        return True

def get_link(content):
    if re.search(u'href=\"(.*?)\"', content):
        return content

def check_for_ico(content):
    link = get_link(content)
    if re.search(u'\.ico\"', link):
        return True

def check_for_png(content):
    link = get_link(content)
    if re.search(u'\.png\"', link):
        return True


@step('at least one should contain rel=\"icon\" and be .png format')
def step_impl(context):
    for tag in context.icon_links:
        tag = str(tag)
        if check_for_rel_icon(tag) and check_for_png(tag):
            tag_found = True
    assert 'tag_found' in locals(), 'Did not find rel=\"shortcut icon\" and ' \
        ' be .png format in %s' % str(context.icon_links)


@step('at least one should contain rel=\"shortcut icon\" and be .ico format')
def step_impl(context):
    for tag in context.icon_links:
        tag = str(tag)
        if check_for_rel_shortcut_icon(tag) and check_for_ico(tag):
            tag_found = True
    assert 'tag_found' in locals(), 'Did not find rel=\"icon\" and ' \
        ' be .ico format in %s' % str(context.icon_links)


@step('I check the console logs')
def check_console(context):
    context.console_errors = []
    for entry in context.driver.get_log('browser'):
        try:
            assert "SEVERE" not in entry['level']
        except AssertionError:
            context.console_errors.append(
                "On Page: %s. Expeced no errors in log instead got:\n%s" % (
                    context.current_url,
                    str(entry)
                )
            )

@step('there should be no severe console log errors')
def check_console_errors(context):
    assert len(context.console_errors) == 0, loop_thru_messages(context.console_errors)
    # try:
    #     assert len(context.console_errors) == 0
    # except AssertionError:
    #     raise LoopThruMessagesException(context.console_errors)


@step('I throttle network speed to "{down:f}" MB/s down, "{up:f}" MB/s up, with "{latency:f}" ms latency')
def step_impl(context, down, up, latency):
    log.info('Toggling speeds with ' + str(down) + ' down and ' + str(up) + ' up')
    conversion = 18000
    log.info('Setting throttle converted to %d' % int(down * conversion))
    context.driver.set_network_conditions(
        offline=False,
        latency=latency,  # additional latency (ms)
        download_throughput=down * conversion,  # maximal throughput
        upload_throughput=up * (conversion * 2)
        # download_throughput=down * 8000,  # maximal throughput
        # upload_throughput=up * 8000
    )

@step('I look for html validator messages')
def step_impl(context):
    context.html_validation_errors = []
    time.sleep(2)
    for entry in context.driver.get_log('browser'):
        if 'console-api' in entry['message']:
            if 'Document is valid' not in entry['message']:
                context.html_validation_errors.append(
                    'On Page: %s. Expected no html validator messages in log ' \
                    'instead got:\n%s' % (
                        context.current_url,
                        str(entry)
                    )
                )

@step('it should not have any validation errors')
def step_impl(context):
    assert len(context.html_validation_errors) == 0, loop_thru_messages(context.html_validation_errors)
    # try:
    #     assert len(context.html_validation_errors) == 0
    # except AssertionError:
    #     raise LoopThruMessagesException(context.html_validation_errors)
