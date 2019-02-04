import json
import requests
from qa.settings import SLACK_URL, SLACK_CHANNEL
from qa.settings import ALLURE_REPORT_HUB_URL, ALLURE_PROJECT_NAME


class SlackMessage(object):

    def __init__(self):
        pass

    def store_exception_context(self, step_name, exception):
        self.exception = 'On Scenario: %s\nFeature: %s\nStep: %s\n%s\n' % (
            self.scenario.name,
            self.feature.name,
            step_name,
            exception
        )
        self.exc_traceback = sys.exc_info()[2]

    def send_message(self, message):
        payload = {
            'channel': SLACK_CHANNEL,
            'icon_emoji': ':vvv:',
            'text': message,
            'username': 'QA Test'
        }
        payload = json.dumps(payload)
        headers = {'Content-Type: application/json'}
        r = requests.post(SLACK_URL, data=payload)
        assert r.status_code == 200, 'Sending Slack Mesage: Got a %s status code with message:\n%s' % (
            r.status_code,
            r.text
        )


    def send_report_generated_message(self):
        assert SLACK_URL is not None and SLACK_CHANNEL is not None,\
            'Please set SLACK_URL and/or SLACK_CHANNEL in settings.py' 
        message = 'Test reports updated at %s/projects/%s/report/index.html#/' % (
            ALLURE_REPORT_HUB_URL,
            ALLURE_PROJECT_NAME
        )
        payload = {
            'channel': SLACK_CHANNEL,
            'icon_emoji': ':microscope:',
            'text': message,
            'username': 'QA Tests'
        }
        payload = json.dumps(payload)
        headers = {'Content-Type': 'application/json'}
        r = requests.post(SLACK_URL, data=payload, headers=headers)
        assert r.status_code == 200, 'Sending Slack Mesage: Got a %s status code with message:\n%s' % (
            r.status_code,
            r.text
        )
