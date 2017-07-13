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
curl -L https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip | tar xz -C env/bin
```
* pip install chromedriver_installer==0.0.6 not working in python 3.6 due to certificate issue

#### Safari setup
To test in Safari you must turn on automation in the dev menu, (Develop > Allow Remote Automation) and directly run webdriver once to authorize permissions (In Terminal: /usr/bin/safaridriver -p 8000).

## Running Tests
Be sure to source virtualenv (```source env/bin/activate```) before running tests.

#### Single File.
You can run a test with this command.
```
python3 path/to/file.py
```

#### Run all tests.

```
behave e2e/features
```

#### Changing domain or browser
The Driver default, base url, and other variables are being defaulted in the environment_variables.py but can be overwritten on the command line.
```
DRIVER='chrome' BASE_URL='http://localhost:3000' behave e2e/features
```


#### Running Single tests.
You can include or exclude tests with the ```--include``` or ```--exclude``` flags that use feature file names.
```
behave e2e/features -i google -e example
```
Or run a single scenario from a feature with the ```--name``` flag:
```
behave e2e/features -n 'This is a scenario name'
```


### Notes about example tests.

* Useful documentation about selenium and webdriver can be found [here](http://selenium-python.readthedocs.io/) (don't miss the webdriver part [here](http://selenium-python.readthedocs.io/api.html#locate-elements-by). Or if you want to know about [here](http://www.seleniumhq.org/docs/) or [behave integration](http://behave.readthedocs.io/en/latest/tutorial.html), [behave features](https://pythonhosted.org/behave/gherkin.html#given-when-then-and-but).

* To stop getting Python Permission prompts on Chromedriver launch follow these [instructions](http://bd808.com/blog/2013/10/21/creating-a-self-signed-code-certificate-for-xcode/) to create a certificate. Run `. env/bin/activate` once and then stop it to get in the virtual env. It should now say `(env)` on Terminal command line, then run this command, replacing *NAME* with the name of the certificate you created.
```
codesign -s NAME -f `which python`
```

* You may need to change the install gitlab-ci file or makefile for the server environment to a linux or other OS, e.g.:
```
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz | tar xz -C env/bin
```
