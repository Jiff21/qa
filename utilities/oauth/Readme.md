# OAUTH

## Introduction

A helper to obtain a `Authorization: Bearer token` via python.


## Install

[Google's Documentation](https://cloud.google.com/iap/docs/authentication-howto)
Short version

  1. Go to [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
  and create an acccount with the Role "Cloud IAP > IAP-Secured Web App User"
  2. Create JSON Web Token by selecting the 3 dots after creating account and
  select Create Key > JSON (If you put in project make sure it gets added to .gitignore)
  3. Confirm the address has been added to [IAP](https://console.cloud.google.com/iam-admin/IAPproject?)
  4. While in [IAP](https://console.cloud.google.com/iam-admin/IAPproject?)
  get the CLIENT ID by clicking on the 3 dots for Google App Engine and selecting
  Edit OAUTH Client (don't regenerate just take Client ID that appears on that page)
  5. Add `export GOOGLE_APPLICATION_CREDENTIALS='/Users/USER/Downloads/example.json`
  with path to the json token and `export CLIENT_ID=fake_id` as well.
  6. source qa/env/bin/activate
  7. `pip3 install -U -r qa/utilities/oauth/requirements.txt`
  8. Run Seleniume Related tests with the following authed driver

```bash
  DRIVER=authenticated_chrome behave qa/functional/features
```


## Switching tests

Example of how to add to locustfile.

```python
from qa.utilities.oauth.service_account_auth import make_iap_request

# Add this to login function
code, bearer_header = make_iap_request(BASE_URL, CLIENT_ID)
assert code == 200, 'Did not get 200 creating bearer token: %d' % (
    code
)
self.custom_headers = {
    "Authorization": bearer_header["Authorization"]
}

```

## Then add the header to all your requests

```python
@task(1)
def index(self):
    self.client.get('/build/', headers=custom_headers)
```


To add it to functional or analytics change the browser import and call an
authed browser.

```python
from qa.functional.features.auth_browser import Browser
```
