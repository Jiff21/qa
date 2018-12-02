import requests
import json
import re
import subprocess
from qa.settings import HOST_URL, LIGHTHOUSE_IMAGE
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.accessibility.write import write_json, write_html
from qa.accessibility.features.environment import FILE_NAME, PAGE, FORMAT

all_pages = PAGES_DICT


for page in all_pages:
    headers = {
        'Accept-Charset': 'UTF-8',
        'Content-Type': 'application/json',
        'X-API-KEY': '<YOUR_API_KEY>'
    }
    print('Scanning')
    print(HOST_URL + PAGES_DICT[page])
    r = requests.get(
        LIGHTHOUSE_IMAGE + '/stream?format=' + FORMAT + '&url=' + HOST_URL + PAGES_DICT[page],
        headers=headers
    )

    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)
    print (urls)

    current_name = FILE_NAME

    req = requests.get(urls[0], headers=headers)
    if FORMAT.lower() == 'json':
        write_json(req, QA_FOLDER_PATH, current_name, PAGES_DICT[page])
    elif FORMAT.lower() == 'html':
        write_html(req, QA_FOLDER_PATH, current_name, PAGES_DICT[page])
    else:
        print('Unrecognized format')


for page in all_pages:
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
