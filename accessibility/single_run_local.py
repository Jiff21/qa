import os
import json
import requests
from qa.settings import HOST_URL
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.accessibility.write import write_json, write_html
from qa.accessibility.features.environment import FILE_NAME, PAGE, FORMAT
from qa.utilities.oauth.service_account_auth import make_iap_request
import subprocess

from qa.settings import HOST_URL, CLIENT_ID
from qa.accessibility.auth_lighthouse import Authed_Lighthouse

lighthouse = Authed_Lighthouse()
escaped_headers = lighthouse.escaped_login(HOST_URL, CLIENT_ID)
lighthouse_json = lighthouse.get_page(escaped_headers, HOST_URL, '')
lighthouse.write_json(lighthouse_json, '')
# def login():
#     '''This would be useful for loading into oauth'''
#     # IAP OAUTH LOGIN
#     user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
#     code, bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
#     assert code == 200, 'Did not get 200 creating bearer token: %d' % (
#         code
#     )
#     stringified_code = str(bearer_header['Authorization'])
#     headers = {
#         'Authorization': stringified_code,
#         'User-Agent': user_agent,
#     }
#     return headers
#
# headers = login()
# print(json.dumps(json.dumps(headers)))

# headers = {
#     "X-Extra-Headers": json.dumps(json.dumps(headers))
# }
#
# page = ''
# generated_command = 'http://localhost:8080/lighthouse?url=%s' % (HOST_URL + page)
#
# print(generated_command)
# r = requests.get(generated_command, headers=headers)
#
# if  r.status_code != requests.codes.ok:
#     assert r.status_code == requests.codes.ok, '%s\n%s' % (str(r.status_code), str(r.text))
# else:
#     file_path = '%s/accessibility/output/%s.json' % (
#         QA_FOLDER_PATH,
#         page
#     )
#     with open(file_path, 'w+') as f:
#         f.write(r.text)

# generated_command = 'lighthouse %s --output=json --output-path=./qa/accessibility/output/%s.json --extra-headers %s' % (
#     HOST_URL,
#     PAGE,
#     json.dumps(json.dumps(headers))
# )
# process = subprocess.Popen(
#     generated_command,
#     stderr=subprocess.STDOUT,
#     shell=True
# )
# process.wait()
