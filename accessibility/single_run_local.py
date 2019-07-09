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
