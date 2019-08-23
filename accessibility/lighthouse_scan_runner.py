import json
import os
import requests
import re
import subprocess
from qa.settings import log
from qa.settings import CLIENT_ID, HOST_URL, IAP_ON
from qa.settings import LIGHTHOUSE_IMAGE, LIGHTHOUSE_SKIPS
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.accessibility.auth_lighthouse import AuthedLighthouse
from qa.accessibility.no_auth_lighthouse import NoAuthLighthouse

file_path = os.path.abspath(os.path.dirname(__file__))
page_report_path = os.path.normpath('output/')
output_directory = os.path.join(
    file_path,
    page_report_path

)


# SHould probably move this into non-authed and then only auth if necessary but testing for now.
sites_to_scan = {}
for page in PAGES_DICT:
    if page in LIGHTHOUSE_SKIPS:
        continue
    else:
        sites_to_scan[page] = PAGES_DICT[page]

lighthouse = NoAuthLighthouse()
if IAP_ON is True:
    auth_lighthouse = AuthedLighthouse()
    escaped_headers, unescaped_headers = auth_lighthouse.escaped_login(HOST_URL, CLIENT_ID)

for page in sites_to_scan:
    if IAP_ON is True:
        r = requests.get(HOST_URL + sites_to_scan[page], headers=unescaped_headers)
        assert r.status_code is requests.codes.ok, 'Unexpectedly got a %d ' \
            'response from page before triggering scanner for %s'  % (
                r.status_code,
                HOST_URL + sites_to_scan[page]
            )
        lighthouse_json = auth_lighthouse.get_page(escaped_headers, HOST_URL, sites_to_scan[page])
    else:
        r = requests.get(HOST_URL + sites_to_scan[page])
        assert r.status_code is requests.codes.ok, 'Unexpectedly got a %d ' \
            'response from page before triggering scanner for %s'  % (
                r.status_code,
                HOST_URL + sites_to_scan[page]
            )
        lighthouse_json = auth_lighthouse.get_page(HOST_URL, sites_to_scan[page])
    lighthouse.write_json(lighthouse_json, page, output_directory)
