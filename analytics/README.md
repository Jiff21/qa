# End-to-End

## Introduction

This is a modified set up of End-to-End, that loads the
[Google Analytics Debug Extension](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna/related?hl=en)
as part of the selenium options. Then uses behave tests to make sure
analytics fire.


## Install

*(if you didn't install as part of main README.MD)*
Create a virtualenv if not already.

```bash
virtualenv -p python3 qa/env
```

Install dependencies to virtualenv.

```bash
source env/bin/activate
pip3 install -r qa/analytics/requirements.txt
. qa/utilities/driver_update/geckodriver.sh
. qa/utilities/driver_update/chromedriver.sh
cp qa/analytics/ga_tracker.crx qa/env/bin
```

* pip install chromedriver_installer==0.0.6 not working in python 3.6 due to certificate issue


## Running Tests

Be sure to source virtualenv (```source qa/env/bin/activate```) before running tests.

```bash
DRIVER=ga_chrome HOST_URL=https://www.google.com behave qa/analytics/features
```


## Updating the Extension

Install [Chrome Extension Source Viewer](https://chrome.google.com/webstore/detail/chrome-extension-source-v/jifpbeccnghkjeaalbbjmodiffmgedin).
Go to the [analytics debugger extension in the store](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna/related?hl=en)
and use the Extension Source Viewer to download a zip file of the extension.
Edit debug = true in background.js
Turn on Dev Mode in the Chrome Extensions Window. Use the Pack Extension button to make a file called ga_tracker.crx.
Look into these pip packages:
crxmake
crx_unpack
(Make seems to depend on but global)pyopenssl==17.2.0
