# OAUTH

## Introduction

A helper to obtain a `Authorization: Bearer token` via python.


## Install

[Google's Documentation](https://cloud.google.com/iap/docs/authentication-howto)
Short version
  1. Go to https://console.cloud.google.com/iam-admin/serviceaccounts and create a service account.
  2. Create JSON Web Token from the service account and save it (If you put in project make sure it gets added to .gitignore)
  3. Grab the email account in the Service Account ID column
  4. Add that email to your Identity-Aware Proxy https://console.cloud.google.com/iam-admin/iap
  5. Go to https://console.cloud.google.com/apis/credentials, click Create CLIENT ID and select OAUTH Client ID
  6. Click on the name of the created OAuth 2.0 Client ID and take note of Client ID and Client Secret.
  7. Add `export GOOGLE_APPLICATION_CREDENTIALS='/Users/USER/Downloads/example.json` with path to the json token and `export CLIENT_ID=fake_id` as well.
  8. source qa/pytwo_env/bin/activate
  9. `pip install -I https://github.com/pypa/pip/archive/master.zip#egg=pip`
  9. `pip install -r qa/utilities/oauth/requirements.txt`
  10. Run file like this:
```
  DRIVER=authenticated_chrome behave qa/functional/features
```


# Switching tests.

Example of how to add to locustfile.
```
from qa.utilities.oauth.service_account_auth import make_iap_request
code, bearer_header = make_iap_request(BASE_URL, CLIENT_ID)
assert code == 200, 'Did not get 200 creating bearer token: %d' % (
    code
)
custom_headers = {
    "Authorization": bearer_header["Authorization"]
}
...
# Then add the header to all your requests.
...
@task(1)
def index(self):
    self.client.get('/build/', h=custom_headers)
```

To add it to functional or analytics change the browser import and call an authed browser.
```from qa.functional.features.auth_browser import Browser```
