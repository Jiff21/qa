import requests
from qa.settings import log, default_headers
from qa.settings import HOST_URL, QA_ENV, USER_EMAIL


class SetupRequests(object):
    '''Setup for requests session used in the various auth files'''

    def __init__(self):
        log.debug('Setting up requests')

    def setup_session(self, bearer_header=None):
        session = requests.Session()
        session.headers.update(default_headers)
        if bearer_header is not None:
            session.headers.update(bearer_header)
        if QA_ENV == 'local':
            login_url = '%s/_ah/login?email=%s.com&admin=True&action=Login&continue=%%2F%%2Flocalhost%%3A3000%%2F' % (
                HOST_URL,
                USER_EMAIL.replace('@', '%40')
            )
            r = session.get(login_url)
        return session
