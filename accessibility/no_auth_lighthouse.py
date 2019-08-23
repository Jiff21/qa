import os
import json
import requests
from qa.settings import log
from qa.settings import HOST_URL, LIGHTHOUSE_IMAGE, default_headers
from qa.settings import QA_FOLDER_PATH


class NoAuthLighthouse(object):

    def __init__(self):
        pass


    def get_page(self, url, uri):
        '''This gets the lighthouse results for the page.'''
        log.debug('Headers for lighthouse request:\n%s' % default_headers)
        full_url = url + uri
        log.debug('full_url for lighthouse request:\n%s' % full_url)
        generated_command = '%s/lighthouse?url=%s' % (LIGHTHOUSE_IMAGE, full_url)
        log.debug('Generated Command for lighthouse is %s' % generated_command)
        r = requests.get(generated_command, headers=default_headers)
        if  r.status_code != requests.codes.ok:
            assert r.status_code == requests.codes.ok, '%s\n%s\ncommand:\n%s' % (
                str(r.status_code),
                str(r.text),
                str(generated_command)
            )
        else:
            return r.text

    def write_json(self, text, page, directory):
        page = page.replace(' ', '_')
        if page == '/' or page == '':
            page = 'index'
        file_path = '%s/accessibility/output/%s.report.json' % (
            QA_FOLDER_PATH,
            page
        )
        log.debug('Writing json to path %s' % file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(file_path, 'w+') as f:
            f.write(text)

    def write_html(self, data, page):
        page = page.replace(' ', '_')
        if page == '/' or page == '':
            page = 'index'
        file_path = '%s/accessibility/output/%s.report.html' % (
            QA_FOLDER_PATH,
            page
        )
        data = response.content
        data.decode('utf-8')
        log.debug('Writing html to path %s' % file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(file_path, 'w') as f:
            f.write(data)
            f.close()
