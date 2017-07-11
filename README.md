# Ballz
* Behave
* Appitools Eyes
* Locust
* Lighthouse
* Zap
*

Weather you catch it now or catch it later when you break the build you still say "balls...", why catch it now.

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
class Accounts:

    def __init__(self):
        print ('Accounts loaded.')

    api_key = 'ENTER_KEY_HERE'

    # Admin Email and password for CMS Testing
    admin_dict = {
        'https://bynd.com': 'https://example-admin.com/example-admin-uri',
        'https://www.testing.appspot.com': 'https://www.testing.appspot.com/example-admin-uri',
        'https://www.dev.appspot.com': 'https://www.dev.appspot.com/example-admin-uri',
        'https://www.staging.appspot.com': 'https://ewww.staging.appspot.com/example-admin-uri'
    }

    admin_email = 'fakeUser1@gmail.com'
    admin_password = ''
    admin_name = 'Admin'

```


\* Also Webdriver, Unittest, Hamcrest and Selenium probably
