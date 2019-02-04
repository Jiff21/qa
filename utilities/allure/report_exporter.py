import os
import requests
from qa.settings import  ALLURE_REPORT_HUB_URL, ALLURE_PROJECT_NAME
from qa.settings import ALLURE_HUB_CLIENT_ID, QA_DIRECTORY
from qa.settings import SLACK_CHANNEL
from qa.utilities.oauth.service_account_auth import make_iap_request
from qa.utilities.slack.webhook import SlackMessage


SEND_FILE_URL = ALLURE_REPORT_HUB_URL + '/upload_file'

code, bearer_header = make_iap_request(ALLURE_REPORT_HUB_URL, ALLURE_HUB_CLIENT_ID)
assert code == 200, 'Did not get 200 creating bearer token: %d' % (
    code
)

headers = {
    "Authorization": bearer_header["Authorization"]
}

data = {'project':ALLURE_PROJECT_NAME}
print('Project is %s' % data['project'])

directory = os.path.join(QA_DIRECTORY,'utilities', 'allure', 'allure_results')
print('Send file to: %s' % SEND_FILE_URL)
for file in os.listdir(directory):
    if '.json' in str(file) or 'history' in str(file) or 'properties' in str(file):
        print('Sending %s' % file)
        files = {'file': open(os.path.join(directory, file), 'rb')}
        r = requests.post(SEND_FILE_URL, files=files, headers=headers, data=data)
        r.raise_for_status()

data = {'project':ALLURE_PROJECT_NAME}
r = requests.post(ALLURE_REPORT_HUB_URL + '/build_report', headers=headers, data=data)
r.raise_for_status()


def send_slack_message():
    slack = SlackMessage()
    slack.send_report_generated_message()

if SLACK_CHANNEL is not None:
    send_slack_message()



#######
# Without IAP example
#######

# SEND_FILE_URL = ALLURE_REPORT_HUB_URL + '/upload_file'
#
# data = {'project':ALLURE_PROJECT_NAME}
# print('Project is %s' % data['project'])
#
# directory = os.path.join(os.path.abspath(os.path.dirname(__file__)),'utilities/allure/allure_results/')
# print('Send file to: %s' % SEND_FILE_URL)
# for file in os.listdir(directory):
#     if '.json' in str(file) or 'history' in str(file) or 'properties' in str(file):
#         print('Sending %s' % file)
#         files = {'file': open(os.path.join(directory, file), 'rb')}
#         r = requests.post(SEND_FILE_URL, files=files, data=data)
#         r.raise_for_status()
#         print(r.text)
#
# data = {'project':ALLURE_PROJECT_NAME}
# r = requests.post(ALLURE_REPORT_HUB_URL + '/build_report', data=data)
# r.raise_for_status()
