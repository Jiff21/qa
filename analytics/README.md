# End-to-End

## Introduction

This is a modified set up of End-to-End, that loads the [Google Analytics Debug Extension](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna/related?hl=en) as part of the selenium options. Then uses behave tests to make sure analytics fire.


## Install
*(if you didn't use main setup.sh script)*
Create a virtualenv if not already.
```
virtualenv -p python3 qa/env
```
Install dependencies to virtualenv.
```
source env/bin/activate
pip3 install -r qa/analytics/requirements.txt
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-macos.tar.gz | tar xz -C qa/env/bin
curl -L https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip | tar xz -C qa/env/bin
cp qa/analytics/ga_tracker.crx qa/env/bin
```
* pip install chromedriver_installer==0.0.6 not working in python 3.6 due to certificate issue

## Running Tests
Be sure to source virtualenv (```source qa/env/bin/activate```) before running tests.

```
BASE_URL=https://www.google.com/about/products behave qa/analytics/features
```


## Updating the Extension.

Install [Chrome Extension Source Viewer](https://chrome.google.com/webstore/detail/chrome-extension-source-v/jifpbeccnghkjeaalbbjmodiffmgedin). Go to the [analytics debugger extension in the store](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna/related?hl=en) and use the Extension Source Viewer to download a zip file of the extension. Edit debug = true in background.js
Turn on Dev Mode in the Chrome Extensions Window. Use the Pack Extension button to make a file called ga_tracker.crx.
