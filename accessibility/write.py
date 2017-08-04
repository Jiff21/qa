# -*- coding: utf-8 -*-
import json
import os


def write_json(response, qa_path, file_name, page):
    data = response.json()
    directory = '%saccessibility/output/' % qa_path
    if page == '/' or page == '':
        file_path = '%s.report.json' % file_name
    else:
        file_path = '%s.report.json' % page.replace('/', '')
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(directory + file_path, 'w') as f:
        json.dump(data, f)


def write_html(response, qa_path, file_name, page):
    data = response.content
    data.decode('utf-8')
    directory = '%saccessibility/output/' % qa_path
    if page == '/' or page == '':
        file_path = '%s.report.html' % file_name
    else:
        file_path = '%s.report.html' % page.replace('/', '')
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(directory + file_path, 'w') as f:
        f.write(data)
        f.close()
