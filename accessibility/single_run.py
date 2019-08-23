import json
import requests
import re
import subprocess
from qa.settings import log
from qa.settings import CLIENT_ID, HOST_URL, IAP_ON
from qa.settings import LIGHTHOUSE_IMAGE, LIGHTHOUSE_SKIPS
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.accessibility.auth_lighthouse import AuthedLighthouse
from qa.accessibility.no_auth_lighthouse import NoAuthLighthouse
from qa.accesssiblity.no_auth_lighthouse import output_directory

SINGLE_LH_URI = os.getenv('SINGLE_URI', '\'')
SINGLE_LH_PAGE_NAME =  os.getenv('SINGLE_LH_PAGE_NAME', 'test page')


lighthouse = NoAuthLighthouse()
if IAP_ON is True:
    auth_lighthouse = AuthedLighthouse()
    escaped_headers = auth_lighthouse.escaped_login(HOST_URL, CLIENT_ID)

if IAP_ON is True:
    r = requests.get(HOST_URL + sites_to_scan[page], headers=unescaped_headers)
    assert r.status_code is requests.codes.ok, 'Unexpectedly got a %d ' \
        'response from page before triggering scanner for %s'  % (
            r.status_code,
            HOST_URL + sites_to_scan[page]
        )
    lighthouse_json = auth_lighthouse.get_page(escaped_headers, HOST_URL, SINGLE_LH_URI)
else:
    assert r.status_code is requests.codes.ok, 'Unexpectedly got a %d ' \
        'response from page before triggering scanner for %s'  % (
            r.status_code,
            HOST_URL + sites_to_scan[page]
        )
    lighthouse_json = auth_lighthouse.get_page(HOST_URL, SINGLE_LH_URI)
lighthouse.write_json(lighthouse_json, SINGLE_LH_PAGE_NAME, output_directory)


# headers = {
#     'Accept-Charset': 'UTF-8',
#     'Content-Type': 'application/json',
#     'X-API-KEY': '<YOUR_API_KEY>'
# }
#
# r = requests.get(
#     LIGHTHOUSE_IMAGE + '/stream?format=' + FORMAT + '&url=' + HOST_URL,
#     headers=headers
# )
#
# # print (r.text)
# urls = re.findall(
#     'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)
# print (urls)
# req = requests.get(urls[0], headers=headers)
#
#
# if FORMAT.lower() == 'json':
#     write_json(req, QA_FOLDER_PATH, FILE_NAME, PAGE)
# elif FORMAT.lower() == 'html':
#     write_html(req, QA_FOLDER_PATH, FILE_NAME, PAGE)
# else:
#     print('Unrecognized format')
