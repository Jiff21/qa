* Behave ([Unit, End-to-End](/functional), and [Analytics](/analytics) tests)
* [Applitools](/visual) (Visual Regression Testing)
* [Locust](/performance) (Performance tests)
* [Lighthouse](/accessibility) (Accessibility & Mobile Support)
* [Zap](/security) (Penetration / Security Tests)
[\*](#caveats)



## Introduction

The BALLZ Stack is a full QA Stack mainly written in python's behave framework.

All of the readme files in this project assume it was cloned into the root of another project and the folder name was kept as 'qa', thus all path commands start with 'qa/'. If you want to try it on it's own before cloning into a project do this.
```
mkdir ballzstack && cd ballzstack
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
Install [python 3](https://www.python.org/downloads/) and [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac) using their .dmg files. Written at Python 3.6.1 for OSX.
Install virtualenv if not already installed.
```
sudo easy_install pip
sudo pip install virtualenv
```
##### Install steps
```
docker pull owasp/zap2docker-stable
docker pull kmturley/lighthouse-ci
. qa/setup.sh
make qa_install
```
Edit the file qa/environment_variables.py to match your development setup(localhost, BASE_URL, Selenium Server, etc), if necessary.
* pip install chromedriver_installer==0.0.6 not working in python 3.6 due to certificate issue. But you may want to add that to requirements.py file for visual, functional, and analytics if you're on 2.7.

##### Setting Local Environment Variables (Optional)
Copy the following text and add it to the end of ```qa/env/bin/activate```, then edit in your credentials so you won't have to add them on the command line when running tests locally. You also want to add these as secret variables on your CI env. The tests in this project should all run off the defaults set in qa/environment_variables (except visual tests), but this an effective way to set env variables locally.
```
export GOOGLE_API_KEY='0123456789'
export EYES_API_KEY='0123456789'
export RECOVERY_EMAIL='another_fake_email@gmail.com'
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

```
###### Service Account Authentication and Identity Aware Proxy (Optional)
If your development environment is protected by IAP, there is a setup for a service account and a chrome that loads an extension that adds Bearer tokens to the header. Follow [mod_header utility setup](utilities/oauth) instructions. Then change browser imports in the feature/environment.py files for analytics and functional to ```from qa.functional.features.auth_browser import Browser```. This is currently only supported for python 2, so you will need to run all the python 3 install in pytwo_env and start running these tests in that virtualenv as well.
```
export CLIENT_ID='########-ksdbjsdkg3893gsbdoi-apps.googleusercontent.com'
export GOOGLE_APPLICATION_CREDENTIALS='path/to/json_token.json'
```
## Running Tests
Instructions for running tests can be found in their individual README.md files.
* [End-to-End](/functional#running-tests)
* [Visual](/visual#running-tests)
* [Analytics](/analytics#running-tests)
* [Performance](/performance#running-tests)
* [Accessibility and Modern Practices](/accessibility#running-tests)
* [Security](/security#running-tests)

#### Run All[\*\*](#caveats) tests

In one terminal window run
```
make zap_serve
```
In another terminal tab:
```
lighthouse_up
```
And in another tab run the following command
```
BASE_URL=https://google.com make test_all
```


---

###### Caveats
\* Technically a couple other things like Webdriver, Unittest, Hamcrest and Selenium were also used. And inevitably a more stuff will be added and I may not change the name.

\*\* I'm not running Applitools with this command as you need account credentials for it to work. If you want to run visual tests fill out qa/accounts.py EYES_API_KEY variable and uncomment run step in makefile.
