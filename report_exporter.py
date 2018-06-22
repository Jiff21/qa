import os
import requests
from qa.settings import  ALLURE_REPORT_HUB_URL, ALLURE_PROJECT_NAME
from qa.utilities.oauth.service_account_auth import make_iap_request


SEND_FILE_URL = ALLURE_REPORT_HUB_URL + '/upload_file'

# HEADERS = {
#     "content-type":"multipart/form-data;",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
# }
data = {'project':ALLURE_PROJECT_NAME}
print('Project is %s' % data['project'])
# http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
# Send a single file example
# files = {'file': open('test.json', 'rb')}
# r = requests.post(ALLURE_REPORT_HUB_URL, files=files, data=data)

directory = os.path.join(os.path.abspath(os.path.dirname(__file__)),'utilities/allure/allure_results/')
print('Send file to: %s' % SEND_FILE_URL)
for file in os.listdir(directory):
    if '.json' in str(file) or 'history' in str(file) or 'properties' in str(file):
        print('Sending %s' % file)
        files = {'file': open(os.path.join(directory, file), 'rb')}
        r = requests.post(SEND_FILE_URL, files=files, data=data)
        r.raise_for_status()

data = {'project':'example'}
r = requests.post(ALLURE_REPORT_HUB_URL + '/build_report', data=data)
r.raise_for_status()
