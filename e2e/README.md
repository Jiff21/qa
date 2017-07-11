# End-to-End

## Introduction

Test written using [Behave Framework](http://pythonhosted.org/behave/) and [Hamcrest Assertions](https://github.com/hamcrest/PyHamcrest)

## Install
Create a virtualenv if not already.
```
virtualenv -p python3 env
```
Install dependencies to virtualenv.
```
source env/bin/activate
pip3 install -r e2e/requirements.txt
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-macos.tar.gz | tar xz -C env/bin
```

#### Safari setup
To test in Safari you must turn on automation in the dev menu, (Develop > Allow Remote Automation) and directly run webdriver once to authorize permissions (In Terminal: /usr/bin/safaridriver -p 8000).

## Running Tests
Be sure to source virtualenv (```source env/bin/activate```) before running tests.

#### Single File.
You can run a test with this command.
```
python3 path/to/file.py
```
 * NOTE: This **will not run** on this project (unless you're running bynd.com locally and start a [selenium/standalone-chrome](https://hub.docker.com/r/selenium/standalone-chrome/) server). I'm leaving default DRIVER on this project as headless_chrome and the default BASE_URL as a localhost address in qa/browser.py. This is because I think the tests should be set to test against a local environment as the BASE_URL and I think we plan on using headless_chrome on docker images as our default testing browser. So I wanted browser.py to look like it should if you copy this over to another project. If you're just checking this out, use the commands in **Changing domain or browser** section below to run against an online url and in normal chrome.


#### Run all tests.

```
behave e2e/features
```

#### Changing domain or browser
In browser.py we setup default base urls and configure what browser get sent to Selenium. These can be overwritten using pythons
[os.getenv](https://docs.python.org/3/library/os.html#process-parameters) passed in before the python command.
```
BASE_URL=https://bynd.com DRIVER=chrome python3 -m unittest discover -s qa/e2e -p *home*.py
DRIVER='chrome' BASE_URL='http://localhost:3000' behave e2e/features
```

#### Suites
If you look at the python-selenium-tests/runner.py file, you can tests are being added to a suite. It's using [sys.argv](https://docs.python.org/2/library/sys.html) to take a command line parameter like 'full' or 'smoke'
to decide what tests to run. Setting suites is optional.
```
BASE_URL=https://bynd.com python3 e2e/suite_runner.py smoke
```


### Notes about example tests.

* Useful documentation can be found [here](http://selenium-python.readthedocs.io/) (don't miss the webdriver part [here](http://selenium-python.readthedocs.io/api.html#locate-elements-by),  and [here](http://www.seleniumhq.org/docs/)).

* To stop getting Python Permission prompts on Chromedriver launch follow these [instructions](http://bd808.com/blog/2013/10/21/creating-a-self-signed-code-certificate-for-xcode/) to create a certificate. Run `. env/bin/activate` once and then stop it to get in the virtual env. It should now say `(env)` on Terminal command line, then run this command, replacing *NAME* with the name of the certificate you created.
```
codesign -s NAME -f `which python`
```

* You may need to add a line to the gitlab-ci file or makefile for the server environment to add geckodriver, it would likely need to use the linux url
```
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz | tar xz -C env/bin
```
