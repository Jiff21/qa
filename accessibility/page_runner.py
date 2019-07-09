import requests
import json
import re
import subprocess
from qa.settings import CLIENT_ID, HOST_URL, LIGHTHOUSE_IMAGE
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.accessibility.write import write_json, write_html
from qa.accessibility.features.environment import FILE_NAME, PAGE, FORMAT
from qa.accessibility.auth_lighthouse import Authed_Lighthouse

# all_pages = PAGES_DICT

lighthouse = Authed_Lighthouse()
escaped_headers = lighthouse.escaped_login(HOST_URL, CLIENT_ID)

# for page in PAGES_DICT:
#     lighthouse_json = lighthouse.get_page(escaped_headers, HOST_URL, page)
#     lighthouse.write_json(lighthouse_json, page)


for page in PAGES_DICT:
    generated_command = ''
    if PAGES_DICT[page] == '/' or PAGES_DICT[page] == '':
        generated_command = 'FILE_NAME=%s behave %saccessibility/features' % (
            'index',
            str(QA_FOLDER_PATH)
        )
    else:
        generated_command = 'FILE_NAME=%s behave %saccessibility/features' % (
            page.replace('/', ''),
            QA_FOLDER_PATH
        )
        print('4 In run behave page' + generated_command)
    process = subprocess.Popen(
        generated_command,
        stderr=subprocess.STDOUT,
        shell=True
    )
    process.wait()
