# Ballz
* Behave
* Appitools Eyes
* Locust
* Lighthouse
* Zap*

Weather you catch it now or catch it later when you break the build you still say "balls...", why not catch it now.

## Overview

* [End-to-End](/e2e)
* [Performance](/perf)
* [Visual](/visual)
* [Pen Testing](/pen)
* [Accessibility](/accessibility)

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


\* Also Webdriver, Unittest, Hamcrest and Selenium probably
