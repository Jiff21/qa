import requests
from qa.settings import log, default_headers


class SetupRequests(object):
    '''Setup for requests session used in the various auth files'''

    def __init__(self):
        log.debug('Setting up requests')

    def setup_session(self, bearer_header=None):
        session = requests.Session()
        session.headers.update(default_headers)
        if bearer_header is not None:
            session.headers.update(bearer_header)

        return session
