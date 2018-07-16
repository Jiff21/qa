* Behave ([Unit, End-to-End](/functional), and [Analytics](/analytics) tests)
* [Galen Framwork](/visual) (Visual Regression Testing)
* [Locust](/performance) (Performance tests)
* [Lighthouse](/accessibility) (Accessibility & Mobile Support)
* [Zap](/security) (Penetration / Security Tests)
[\*](#caveats)


## Introduction

This is a full QA Stack mainly written in python's behave framework.

All of the readme files in this project assume it was cloned into the root of another project and the folder name was kept as 'qa', thus all path commands start with 'qa/'. If you want to try it on it's own before cloning into a project do this.
```
mkdir fake_project && cd fake_project
git clone git@github.com:Jiff21/qa.git qa
```
if you do clone it  into another project:
```
cd path/to/project/folder
git clone git@github.com:Jiff21/qa.git
rm -rf qa/.git
rm -f qa/.gitignore
git add -A
git commit -m "Cloned in test setup"
```

You will also need to add commands to your projects docker-compose.yml, .gitlab-ci.yml or bitbucket-pipelines.yml. There are example CI implementation files in qa/ci_files.


## Install
##### Dependancies
Install [python 3](https://www.python.org/downloads/) and [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac) using their .dmg files. Written at Python 3.6.1 for OSX. Virtualenv (`pip3 install virtualenv`).

##### Install steps
```
docker pull owasp/zap2docker-stable
docker pull kmturley/lighthouse-ci
virtualenv -p python3.6 qa/env
source qa/env/bin/activate
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-macos.tar.gz | tar xz -C qa/env/bin
. qa/utilities/driver_update/chromedriver.sh
cp qa/analytics/ga_tracker.crx qa/env/bin
pip3 install -U -r qa/functional/requirements.txt
pip3 install -U -r qa/security/requirements.txt
pip3 install -U -r qa/analytics/requirements.txt
pip3 install -U -r qa/visual/requirements.txt
pip3 install -U -r qa/accessibility/requirements.txt
pip3 install -U -r qa/performance/requirements.txt
curl -L https://github.com/galenframework/galen/releases/download/galen-2.3.6/galen-bin-2.3.6.zip | tar xy -C qa/env/bin/
cd qa/env/bin/galen-bin-2.3.6 && sudo ./install.sh && cd ../../../../
```
Optional, if you plan on using Allure Reports.
```
pip3 install -U -r qa/utilities/allure/requirements.txt
```

Edit the file qa/settings.py to match your development setup(localhost, BASE_URL, Selenium Server, etc), if necessary.
* pip install chromedriver_installer==0.0.6 not working in python 3.6 due to certificate issue. But you may want to add that to requirements.py file for visual, functional, and analytics if you're on 2.7.

##### Setting Local Environment Variables (Optional)
Copy the following text and add it to the end of ```qa/env/bin/activate```, then edit in your credentials so you won't have to add them on the command line when running tests locally. You also want to add these as secret variables on your CI env. The tests in this project should all run off the defaults set in qa/settings.py (except visual tests), but this an effective way to set env variables locally.
```
export GOOGLE_API_KEY='0123456789'
export EYES_API_KEY='0123456789'

export ZAP_ADDRESS='http://localhost:8080'
export ZAP_API_KEY='0123456789'

export ADMIN_EMAIL='fakeuser1@gmail.com'
export ADMIN_PASSWORD='fakepassword'
export ADMIN_NAME='Al Admin'

export EDITOR_EMAIL='fakeUser2@gmail.com'
export EDITOR_PASSWORD='fakepassword'
export EDITOR_NAME='Eddie Editor'

export USER_EMAIL='fakeUser3@gmail.com'
export USER_PASSWORD='fakepassword'
export USER_NAME='Vinny Testaverde'

export RECOVERY_EMAIL='another_fake_email@gmail.com'
export RECOVERY_CITY='New New York'
export RECOVERY_PHONE='555-555-5555'

```

###### Service Account Authentication and Identity Aware Proxy (Optional)
If your development environment is protected by IAP, there is a setup for a service account and a chrome that loads an extension that adds Bearer tokens to the header. Follow [mod_header utility setup](utilities/oauth) instructions. Then change browser imports in the feature/environment.py files for analytics and functional to ```from qa.functional.features.auth_browser import Browser```.
```
pip3 install -U -r qa/utilities/oauth/requirements.txt
export CLIENT_ID='########-ksdbjsdkg3893gsbdoi-apps.googleusercontent.com'
export GOOGLE_APPLICATION_CREDENTIALS='path/to/json_token.json'
```


## Running Tests
Instructions for running tests individually can be found in their respective README.md files.
* [End-to-End](/functional#running-tests)
* [Visual](/visual#running-tests)
* [Analytics](/analytics#running-tests)
* [Performance](/performance#running-tests)
* [Accessibility and Modern Practices](/accessibility#running-tests)
* [Security](/security#running-tests)

#### Run All[\*](#caveats) Tests
```
cp qa/docker-compose-example.yml docker-compose.yml
docker-compose up
```



---

###### Caveats
[\*] Visual is currently not working due to a fix needed in how Galen fails.

\*\* If you have `export PATH="/usr/local/bin:$PATH"` in your bash_profile this will cause a module not found for some python imports. I suggest setting your python path with `export PATH="/Library/Frameworks/Python.framework/Verions/3.6/bin:${PATH}"` & `export PATH="~/Library/Python/2.7/bin:$PATH"`
