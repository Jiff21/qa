import os
import json
import re
import requests
from qa.settings import BASE_URL, LIGHTHOUSE_IMAGE
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.accessibility.write import write_json, write_html
from qa.accessibility.features.environment import FILE_NAME, PAGE, FORMAT


headers = {
    'Accept-Charset': 'UTF-8',
    'Content-Type': 'application/json',
    'X-API-KEY': '<YOUR_API_KEY>'
}

r = requests.get(
    LIGHTHOUSE_IMAGE + '/stream?format=' + FORMAT + '&url=' + BASE_URL,
    headers=headers
)

# print (r.text)
urls = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)
print (urls)
req = requests.get(urls[0], headers=headers)


if FORMAT.lower() == 'json':
    write_json(req, QA_FOLDER_PATH, FILE_NAME, PAGE)
elif FORMAT.lower() == 'html':
    write_html(req, QA_FOLDER_PATH, FILE_NAME, PAGE)
else:
    print('Unrecognized format')
