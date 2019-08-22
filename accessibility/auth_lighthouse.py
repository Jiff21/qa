import os
import json
import requests
from qa.settings import log
from qa.settings import HOST_URL, LIGHTHOUSE_IMAGE
from qa.settings import PAGES_DICT, QA_FOLDER_PATH
from qa.accessibility.write import write_json, write_html
from qa.accessibility.features.environment import FILE_NAME, PAGE, FORMAT
from qa.utilities.oauth.service_account_auth import make_iap_request
import subprocess

from qa.settings import HOST_URL, CLIENT_ID


class Authed_Lighthouse:

    def __init__(self):
        pass

    def escaped_login(self, host, id_for_client):
        log.debug('Getting escaped login headers.')
        '''Lighthouse wants escaped double quotes for the headers passed to --extra-headers flag'''
        
        code, bearer_header = make_iap_request(host, id_for_client)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        stringified_code = str(bearer_header['Authorization'])
        headers = {
            'Authorization': stringified_code,
        }
        log.debug('These are the escaped headers:\n%s' % json.dumps(json.dumps(headers)))
        return json.dumps(json.dumps(headers))


    def get_page(self, escaped_headers, url, page):
        '''This gets the lighthouse results for the page.'''
        headers = {
            "X-Extra-Headers": escaped_headers
        }
        log.debug('Headers for lighthouse request:\n%s' % headers)
        full_url = url + page
        log.debug('full_url for lighthouse request:\n%s' % full_url)
        generated_command = '%s/lighthouse?url=%s' % (LIGHTHOUSE_IMAGE, full_url)
        log.debug('Generated Command for lighthouse is %s' % generated_command)
        r = requests.get(generated_command, headers=headers)
        if  r.status_code != requests.codes.ok:
            assert r.status_code == requests.codes.ok, '%s\n%s\ncommand:%' % (
                str(r.status_code),
                str(r.text),
                generated_command
            )
        else:
            return r.text

    def write_json(self, text, page):
        if page == '/' or page == '':
            page = 'index'
        file_path = '%s/accessibility/output/%s.report.json' % (
            QA_FOLDER_PATH,
            page
        )
        log.debug('Writing json to path %s' % file_path)
        with open(file_path, 'w+') as f:
            f.write(text)
