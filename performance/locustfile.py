from locust import HttpLocust, TaskSet, task, between
from qa.settings import PAGES_DICT
from qa.settings import HOST_URL, CLIENT_ID
# Import needed for IAP login
# from qa.utilities.oauth.service_account_auth import make_iap_request
# Import needed for basic login
# from qa.utilities.oauth.basic_auth_headers import get_encoded_auth_token

def login():
    '''Login function for service accounts with Web App User permission'''
    code, bearer_header = make_iap_request(HOST_URL, CLIENT_ID)
    assert code == 200, 'Did not get 200 creating bearer token: %d' % (
        code
    )
    return bearer_header['Authorization']


def basic_auth():
    '''Login function for service accounts with Web App User permission'''
    auth_token = get_encoded_auth_token()
    return auth_token


# Uncomment if you wan to use one them for login
# token = login()
# token = basic_auth()

class UserBehavior(TaskSet):

    def on_start(self):
        """ on_stop is called when the TaskSet is starting """
        # Set bearer headers if not on live environment that has IAP off.
        if 'https://example.com' not in HOST_URL:
            self.client.headers['Authorization']= token
            # if using cookies can be updated similarly
            # self.locust.client.cookies.update(self.cookies)
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    # Weighting likelyhood of request to this function
    @task(10)
    def index(self):
        self.client.get('%s' % PAGES_DICT['index'])

    @task(1)
    def about(self):
        self.client.get('%s' % PAGES_DICT['about'])

    @task(3)
    def contact(self):
        '''This one is checking we are getting pased oauth wall which 200s'''
        # Don't check on first taska setup can effect first host and mislead you
        with self.client.get(
            '%s' % PAGES_DICT['contact'],
            catch_response=True
        ) as r:
            if HOST not in r.url:
                print('Did not get expected url, instead %s' % (
                    r.url
                ))
                exit(1)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 30)
