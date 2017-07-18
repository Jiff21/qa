* [Behave](/e2e) (Unit and End-to-End tests)
* [Applitools](/visual) (Visual Regression Testing)
* [Locust](/perf) (Performance tests)
* [Lighthouse](/accessibility) (Accessibility & Mobile Support)
* [Zap](/pen) (Penetration / Security Tests)
[\*](#caveats)



## Introduction

The BALLZ Stack is a full QA Stack mainly written in python's behave framework.

All the readmes in this project assume it was cloned into the root of another project and the folder name was kept as 'qa', thus all path commands start with 'qa/'. If you want to try it on it's own before cloning into a project do this.
```
mkdir ballzstack && cd ballzstack
git clone git@github.com:Jiff21/qa.git qa
```
WIP - Just started  this so it's very WIP. But everything except Appitools is set up to run now.

## Install
##### Dependancies
Install [python 3](https://www.python.org/downloads/) and [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac) using their .dmg files. Written at Python 3.6.1 for OSX.
Install virtualenv if not already installed.
```
pip3 install virtualenv
```
##### Install steps
```
. qa/setup.sh
make qa_install
```

Edit the file environment_variables.py in the root of this project to match your development setup if necessary.

##### Accounts File
Add an a file ```qa/accounts.py``` and paste in the code below. Then edit in your credentials.
```
import os


class Accounts:

    def __init__(self):
        print ('Accounts loaded.')

    GOOGLE_API_KEY = 'ENTER_KEY_HERE'
    ZAP_API_KEY = '0123456789'
    ZAP_API_IP = '0.0.0.0'
    ZAP_API_PORT = '8090'

    # Admin Email and password for CMS Testing
    ADMIN_DICT = {
        'https://example.com': 'https://example.com/admin-uri',
        'https://www.testing.appspot.com': 'https://www.testing.appspot.com/admin-uri',
        'https://www.dev.appspot.com': 'https://www.dev.appspot.com/admin-uri',
        'https://www.staging.appspot.com': 'https://ewww.staging.appspot.com/admin-uri'
    }

    ADMIN_EMAIL = 'fakeUser1@gmail.com'
    ADMIN_PASSWORD = ''
    ADMIN_NAME = 'Al\' Admin'

    EDITOR_EMAIL = 'fakeUser2@gmail.com'
    EDITOR_PASSWORD = ''
    EDITOR_NAME = 'Eddie Editor'

    USER_EMAIL = 'fakeUser3@gmail.com'
    USER_PASSWORD = ''
    USER_NAME = 'Vinny Testaverde'

```

## Running Tests
Instructions for running tests can be found in their individual README.md files.
* [Behave](/e2e#running-tests)
* [Applitools](/visual)
* [Locust](/perf#running-tests)
* [Lighthouse](/accessibility#running-tests)
* [Zap](/pen#running-tests)

#### Run All tests

In one terminal window run
```
make zap_serve
```

In another run the following command (BASE_URL and ZAP_SERVER_PROXY optional but will let this run without an accounts.py file or somehing running locally)
```
BASE_URL=https://google.com ZAP_SERVER_PROXY=0.0.0.0:8090 make test_all
```


---

###### Caveats
\* Technically a couple other things like Webdriver, Unittest, Hamcrest and Selenium were also used. And inevitably a bunch of other stuff will be added.
