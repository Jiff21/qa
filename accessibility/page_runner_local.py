import os
import json
import requests
import subprocess
from qa.accessibility.write import write_json, write_html
from qa.accessibility.features.environment import FILE_NAME, PAGE, FORMAT
from qa.settings import HOST_URL, CLIENT_ID
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.utilities.oauth.service_account_auth import make_iap_request


def login():
    '''This would be useful for loading into oauth'''
    # IAP OAUTH LOGIN
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    code, bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
    assert code == 200, 'Did not get 200 creating bearer token: %d' % (
        code
    )
    stringified_code = str(bearer_header['Authorization'])
    headers = {
        'Authorization': stringified_code,
        'User-Agent': user_agent,
    }
    return headers

headers = login()

for page in PAGES_DICT:
    generated_command = ''
    if PAGES_DICT[page] == '/' or PAGES_DICT[page] == '':
        output_path = "./qa/accessibility/output/index.json"
        page_name = "%s.json" % page
        generated_command = 'lighthouse %s --output=json --output-path=./qa/accessibility/output/%s --extra-headers %s' % (
            HOST_URL + PAGES_DICT[page],
            output_path,
            json.dumps(json.dumps(headers))
        )
    else:
        output_path = "./qa/accessibility/output/%s.json" % page
        generated_command = 'lighthouse %s --output=json --output-path=%s --extra-headers %s' % (
            HOST_URL + PAGES_DICT[page],
            output_path,
            json.dumps(json.dumps(headers))
        )
    process = subprocess.Popen(
        generated_command,
        stderr=subprocess.STDOUT,
        shell=True
    )
    process.wait()
