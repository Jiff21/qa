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
  8. source qa/locust_env/bin/activate
  9. `pip install -r qa/utilities/oauth/requirements.txt`
  10. Run file like this:
```
  DRIVER=authenticated_chrome behave qa/functional/features
```
