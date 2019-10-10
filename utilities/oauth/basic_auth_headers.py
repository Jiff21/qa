import base64
from qa.settings import BASIC_AUTH_USER, BASIC_AUTH_PASSWORD


def get_basic_auth_headers():
    #WAF is filtering headers without user agents
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865 Safari/537.36"
    headers = {
        'User-Agent': user_agent,
    }
    # If environment has basic auth add it to headers
    if BASIC_AUTH_USER and BASIC_AUTH_PASSWORD:
        usrPass = "%s:%s" % (BASIC_AUTH_USER, BASIC_AUTH_PASSWORD)
        b64Val = base64.b64encode(usrPass.encode())
        headers['Authorization'] = "Basic %s" % b64Val.decode("utf-8")

    return headers


def get_encoded_auth_token():
    # if BASIC_AUTH_USER and BASIC_AUTH_PASSWORD:
    usrPass = "%s:%s" % (BASIC_AUTH_USER, BASIC_AUTH_PASSWORD)
    b64Val = base64.b64encode(usrPass.encode())
    token = "Basic %s" % b64Val.decode("utf-8")

    return token

# Other version
# if BASIC_AUTH_USER and BASIC_AUTH_PASSWORD:
#   self.auth = (BASIC_AUTH_USER, BASIC_AUTH_PASSWORD)
# else:
#   self.auth = None
# # Test user agent to avoid WAF blocking test agents
# user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865 Safari/537.36"
# self.headers = {'User-Agent': user_agent}
# response = self.client.get(HOST_URL, headers=self.headers, auth=self.auth)
# assert response.status_code == 200
# Authentication (THIS Doesn't work but seems close to adding the hea)
