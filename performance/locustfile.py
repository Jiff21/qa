from locust import HttpLocust, TaskSet, task
from qa.settings import PAGES_LIST


class UserBehavior(TaskSet):
    #
    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()
    #
    # def login(self):
    #     '''This would be useful for loading into oauth'''
    #     self.client.post(
    #         "/login", {"username": "ellen_key", "password": "education"})

    @task(1)
    def index(self):
        self.client.get('/')

    @task(2)
    def about(self):
        self.client.get('%s' % PAGES_LIST[0])

    @task(3)
    def contact(self):
        self.client.get('%s' % PAGES_LIST[1])


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
