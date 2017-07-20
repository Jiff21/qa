# End-to-End

## Introduction

Test written using [Behave Framework](http://pythonhosted.org/behave/) and [Hamcrest Assertions](https://github.com/hamcrest/PyHamcrest)

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
BASE_URL=https://letskodeit.teachable.com/p/practice behave qa/analytics/features
```
