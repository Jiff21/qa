# QA Stack

* Behave ([Unit, End-to-End](/functional), and [Analytics](/analytics) tests)
* [Galen Framwork](/visual) (Visual Regression Testing)
* [Locust](/performance) (Performance tests)
* [Lighthouse](/accessibility) (Accessibility & Mobile Support)
* [Zap](/security) (Security Tests)


## Introduction

This is a full QA Stack mainly written in python's behave framework.

All of the readme files in this project assume it was cloned into the root of
another project and the folder name was kept as 'qa', thus all path commands
start with 'qa/'. If you want to try it on it's own before cloning into a
project do this.

```bash
mkdir fake_project && cd fake_project
git clone git@github.com:Jiff21/qa.git qa
```

if you do clone it into another project:

```bash
cd path/to/project/folder
git clone git@github.com:Jiff21/qa.git
rm -rf qa/.git
rm -f qa/.gitignore
git add -A
git commit -m "Cloned in test setup"
```

If you plan to integrate this into CI, you obviously add commands & environment
variables[<sup>1</sup>](#1-pipeline-variables) to your projects
docker-compose.yml, .gitlab-ci.yml or bitbucket-pipelines.yml. There are example
CI implementation files in qa/ci_files.


## Install

### Dependancies

Install [python 3](https://www.python.org/downloads/) and
[Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac)
using their .dmg files. Written at Python 3.6.1 for OSX. Virtualenv (`pip3 install virtualenv`).

### Install steps

```bash
virtualenv -p python3.6 qa/env
source qa/env/bin/activate
. qa/utilities/driver_update/geckodriver.sh
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

Edit the file qa/settings.py to match your development setup (localhost,
HOST_URL, Selenium Server, etc) if you're using this for another site.


## Running Tests

Instructions for running tests individually can be found in their respective README files.

* [End-to-End](/functional#running-tests)
* [Visual](/visual#running-tests)
* [Analytics](/analytics#running-tests)
* [Performance](/performance#running-tests)
* [Accessibility and Modern Practices](/accessibility#running-tests)
* [Security](/security#running-tests)

### Run All Tests

Using docker-compose to run all tests locally is more for demo purposes, but
it seems docker needs more RAM to run all tests at the same time (Preferences >
Advanced > Ram 6.5)

```bash
cp qa/ci_files/docker-compose-example.yml docker-compose.yml
docker-compose up
```

Docker compose will leave allure results on a local folder. So install Allure
and generate a report.

```bash
pip3 install -U -r qa/utilities/allure/requirements.txt
allure generate qa/utilities/allure/allure_results/ -o qa/utilities/allure/allure-reports/ --clean
allure open qa/utilities/allure/allure-reports/
```

See [Allure](/utilities/allure) for more on allure results and generating
history / trends.

### Extras

#### Service Account Authentication and Identity Aware Proxy (Optional)
If your development environment is protected by IAP, there is a setup for a service account
and a chrome that loads an extension that adds Bearer tokens to the header. Follow
[mod_header utility setup](utilities/oauth) instructions. Then change browser imports in
the feature/environment.py files for analytics and functional to
```from qa.functional.features.auth_browser import Browser```.

```bash
pip3 install -U -r qa/utilities/oauth/requirements.txt
export CLIENT_ID='########-ksdbjsdkg3893gsbdoi-apps.googleusercontent.com'
export GOOGLE_APPLICATION_CREDENTIALS='path/to/json_token.json'
```

#### [<sup>1</sup>] Pipeline Variables

The necessary pipeline variables depend on what you're using from this scaffolding.  
If you want to use qa/functional/steps/login.py you need to setup all the account variables.
If you end up send allure reports be sure to add ALLURE_REPORT_HUB_URL, ALLURE_PROJECT_NAME,
ALLURE_HUB_CLIENT_ID. If you're using the Google IAP OATH tool above be sure to set up
CLIENT_ID and GOOGLE_APPLICATION_CREDENTIALS, you past in the content of the file for the
value instead of a path like you use locally.


#### Setting Local Environment Variables (Optional)

Duplicate the file found at qa/secrets/example.env.example and rename it `testing.env`,
`staging.env`, `dev.env`, or `production.env`. Edit the values in that file to match
you environment or in `qa/settings.py` to edit the default/local environment values.
You can now switch between environments while testing by setting a `QA_ENV` variable
(for example `export QA_ENV=testing`).

Or variables for IAP or using a remote allure hub. You also want to add these
as secret variables on your CI env if you plan on running similar tests on CI.
The demo tests in this project should all run off the defaults set in
qa/settings.py.

---

#### Caveats

* If you have `export PATH="/usr/local/bin:$PATH"` in your bash_profile this
will cause a module not found for some python imports. I suggest setting your
python path with
  `export PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"` &
  `export PATH="~/Library/Python/2.7/bin:$PATH"`
* If plan to use performance tests at higher settings you may have to do [this](https://github.com/docker/for-mac/issues/1009) to avoid [this](https://github.com/docker/for-mac/issues/1374).  
In CI you want to stagger security and performance. If you don't do this you'll hit this
[issue](https://github.com/docker/compose/issues/4486), may have to go back to make file.
* pip install chromedriver_installer==0.0.6 not working in python 3.6 due to certificate issue.
  That's why I'm not using it.
* Docker-Compose currently takes up about 5GB of free space with docker images. Want to leave the demo Dockerfile here for demo purposes. For CI all tests off the same
  [docker image](https://hub.docker.com/r/jiffcampbell/qa_baglz/) for pre-built speed.
