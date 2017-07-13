# B.A.L.L.Zstack
* [Behave](/e2e) (Unit and End-to-End tests)
* [Appitools Eyes](/visual) (Visual Regression Testing)
* [Locust](/perf) (Performance tests)
* [Lighthouse](/accessibility) (Accessibility & Mobile Support)
* [Zap](/pen) (Penetration / Security Tests)
[\*](#caveats)

BallzStack is a full stack of qa automation written mostly with behave python tests.

WIP - Just started  this so it's very WIP. But everything except Appitools is set up to run now.

## Full Setup

##### Dependancies
Install python 3 using [dmg](https://www.python.org/downloads/). Written at Python 3.6.1.
Install virtualenv if not already installed.
```
pip3 install virtualenv
```

TBD
```
make setup
```

Edit the file environment_variables.py in the root of this project to match your development setup.

##### Accounts File
Add an accounts.py file to the root directory for storing credentials.
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

###### Caveats
\* Technically a couple other things like Webdriver, Unittest, Hamcrest and Selenium were also used. And inevitably a bunch of other stuff will be added.
