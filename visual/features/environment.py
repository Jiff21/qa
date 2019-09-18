import os
import subprocess
import sys
from behave import *
from qa.functional.features.browser import Browser
from qa.settings import IAP_ON
from qa.functional.features.browser import Browser # Change if using IAP
from qa.utilities.oauth.service_account_auth import make_iap_request

def before_all(context):
    if IAP_ON is True:
        code, context.bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        # Add Bearer headers to browsermob proxy
        context.proxy, context.server = get_proxy_and_server(context.bearer_header)
    process = subprocess.Popen('rm -R qa/visual/images/current_run/*', shell=True, stdout=subprocess.PIPE)
    process.wait()
    print('delete file returned %d' % process.returncode)
    process = subprocess.Popen('rm -R qa/visual/images/diffs/*', shell=True, stdout=subprocess.PIPE)
    process.wait()
    print('delete file returned %d' % process.returncode)


def after_all(context):
    if IAP_ON is True:
        context.server.stop()



# def before_feature(context, feature):

# def after_feature(context, feature):
#


def before_scenario(context, scenario):
    if os.getenv('DRIVER') == 'firefox':
        if "firefoxskip" in scenario.effective_tags:
            sys.stdout.write('firefox not supported for %s' % (scenario))
            scenario.mark_skipped()
    if 'browser' in context.tags:
        context.browser = Browser()
        context.driver = context.browser.get_browser_driver()


def after_scenario(context, feature):
    if 'browser' in context.tags:
        context.driver.quit()
