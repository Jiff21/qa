import requests
import json
import re
import subprocess
from qa.environment_variables import BASE_URL, LIGHTHOUSE_IMAGE
from qa.environment_variables import PAGES_LIST, QA_FOLDER_PATH
from qa.accessibility.write import write_json, write_html
from qa.accessibility.features.environment import FILE_NAME, PAGE, FORMAT

all_pages = PAGES_LIST
all_pages.append('/')

for page in all_pages:
    headers = {
        'Accept-Charset': 'UTF-8',
        'Content-Type': 'application/json',
        'X-API-KEY': '<YOUR_API_KEY>'
    }

    r = requests.get(
        LIGHTHOUSE_IMAGE + '/stream?format=' + FORMAT + '&url=' + BASE_URL + page,
        headers=headers
    )

    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)
    print (urls)

    if page != '/':
        current_name = page.replace('/', '')
    else: 
        current_name = FILE_NAME

    req = requests.get(urls[0], headers=headers)
    if FORMAT.lower() == 'json':
        write_json(req, QA_FOLDER_PATH, current_name, page)
    elif FORMAT.lower() == 'html':
        write_html(req, QA_FOLDER_PATH, current_name, page)
    else:
        print('Unrecognized format')


for page in all_pages:
    generated_command = ''
    if page == '/' or page == '':
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
