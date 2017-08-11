# import google.oauth2.credentials
# from google.auth.transport.requests import AuthorizedSession
#
#
# credentials = google.oauth2.credentials.Credentials(
#     'access_token')
#
# authed_session = AuthorizedSession(credentials)
# response = authed_session.get(
#     'https://sf-campsite-cms-feature.appspot.com/')
# print (response.status_code)


import requests
import httplib
import base64
import urllib
import json
from subprocess import Popen


class ExampleOAuth2Client:
    def __init__(self, client_id, client_secret):
        self.access_token = None

        # OBtained from https://console.cloud.google.com/apis/credentials
        self.service = OAuth2Service(
            name="foo",
            client_id='###-kdkd.apps.googleusercontent.com',
            client_secret='XCZKjzxfkjfdskj',
            access_token_url="https://-strawman.appspot.com/_gcp_gatekeeper/authenticate",
            authorize_url="http://api.example.com/oauth/access_token",
            base_url="https://accounts.google.com/o/oauth2/v2/auth",
        )

        self.get_access_token()

    def get_access_token(self):
        data = {'code': 'bar',
                'grant_type': 'client_credentials',
                'redirect_uri': 'http://example.com/'}

        session = self.service.get_auth_session(data=data, decoder=json.loads)

        self.access_token = session.access_token
