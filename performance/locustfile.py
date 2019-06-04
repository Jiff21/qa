from locust import HttpLocust, TaskSet, task
from qa.settings import PAGES_DICT
from qa.settings import HOST_URL, CLIENT_ID
# from qa.utilities.oauth.service_account_auth import make_iap_request


class UserBehavior(TaskSet):

    # def setup(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     Uncomment if you wan to use login
    #     self.login()

    def login(self):
        '''This would be useful for loading into oauth'''
        # IAP OAUTH LOGIN
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        code, bearer_header = make_iap_request(BASE_URL, CLIENT_ID)
        assert code == 200, 'Did not get 200 creating bearer token: %d' % (
            code
        )
        self.headers = {
            'Authorization': bearer_header['Authorization'],
            'User-Agent': user_agent,
        }
        # Basic Auth Example (from qa.utilities.oauth.basic_auth_headers import get_encoded_auth_token).
        # Delete above and use this instead if you are using basic auth.
        # user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        # self.headers = {
        #     'User-Agent': user_agent,
        # }
        # if 'https://example.com' not in BASE_URL:
        #     self.auth_token = get_encoded_auth_token()
        #     self.headers['Authorization'] = self.auth_token
        #
        # self.locust.client.headers.update(self.headers)
        # # if using cookies can be updated simimalry
        # # self.locust.client.cookies.update(self.cookies)
        # if you have your own login on postself.
        # self.client.post(
        #     "/login", {"username": "ellen_key", "password": "education"}
        # )


    # def on_start(self):
    #     pass

    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping """
    #     pass


    @task(1)
    def index(self):
        self.client.get('%s' % PAGES_DICT['index'])

    @task(2)
    def about(self):
        self.client.get('%s' % PAGES_DICT['about'])

    @task(3)
    def contact(self):
        self.client.get('%s' % PAGES_DICT['contact'])


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
