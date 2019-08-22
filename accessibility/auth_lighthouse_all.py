import json
import requests
import re
import subprocess
from qa.settings import log
from qa.settings import CLIENT_ID, HOST_URL, LIGHTHOUSE_IMAGE
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.accessibility.write import write_json, write_html
from qa.accessibility.features.environment import FILE_NAME, PAGE, FORMAT
from qa.accessibility.auth_lighthouse import Authed_Lighthouse


# SHould probably move this into non-authed and then only auth if necessary but testing for now.

all_pages = PAGES_DICT

lighthouse = Authed_Lighthouse()
escaped_headers = lighthouse.escaped_login(HOST_URL, CLIENT_ID)

# for page in all_pages:
page = '/'
lighthouse_json = lighthouse.get_page(escaped_headers, HOST_URL, page)
lighthouse.write_json(lighthouse_json, page)
