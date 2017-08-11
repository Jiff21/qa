# OAUTH

## Introduction

A helper to obtain a `Authorization: Bearer: token` via python.


## Install

[Google's Documentation](https://cloud.google.com/iap/docs/authentication-howto)
Short version
  1. Go to https://console.cloud.google.com/iam-admin/serviceaccounts and create a service account.
  2. Create JSON Web Token from the service account and save it
  3. Grab the email account in the Service Account ID column
  4. Add that email to your Identity-Aware Proxy https://console.cloud.google.com/iam-admin/iap
  5. Go to https://console.cloud.google.com/apis/credentials, click Create CLIENT Id and select OAUTH Client Id
  6. Click on the name of the created Oauth 2.0 Clinet ID and take note of Client ID and Client Secret.
  7. add `export GOOGLE_APPLICATION_CREDENTIALS='/Users/USER/Downloads/example.json` with path to json token
  8. source qa/locust_env/bin/activate
  9. ```pip install -r qa/utilities/oauth/requirements.txt```
  10. Run file like this:
```
  CLIENT_ID='fake_id' BASE_URL='fakeaddress' GOOGLE_APPLICATION_CREDENTIALS=/fake/path/to/application python qa/analytics/oauth2.py'
```
