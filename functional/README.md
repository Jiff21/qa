# End-to-End

## Introduction

Test written using [Behave Framework](http://pythonhosted.org/behave/).

## Install
*(if you didn't install as part of main README.MD)*
Create a virtualenv if not already.

```bash
virtualenv -p python3.6 qa/env
```

Install dependencies to virtualenv.

```bash
source qa/env/bin/activate
pip3 install -U -r qa/functional/requirements.txt
. qa/utilities/driver_update/geckodriver.sh
. qa/utilities/driver_update/chromedriver.sh
```

#### Safari setup
To test in Safari you must turn on automation in the dev menu, (Develop > Allow
Remote Automation) and directly run webdriver once to authorize
permissions (In Terminal: /usr/bin/safaridriver -p 8000).

## Running Tests
Be sure to source virtualenv (```source qa/env/bin/activate```) before
running tests.

#### Run all tests.

```bash
behave qa/functional/features
```

#### Changing domain or browser
The Driver default, base url, and other variables are being defaulted in the
`qa/settings.py` but can be overwritten on the command line.

```bash
DRIVER=chrome HOST_URL=https://google.com behave qa/functional/features/
```

#### Running Single files or tests
Behave breaks things up by **features**. A feature is what it sounds like, it
might have several user stories or as Behave calls them **scenarios**,
You can include or exclude tests with the ```--include``` or ```--exclude```
flags that use feature file names.

```bash
behave qa/functional/features -i example -e other_file_name
```

Or run a single scenario from a feature with the ```--name``` flag.

```bash
behave qa/functional/features -n 'This is a scenario name'
```

There's a bug in selenium/standalone-chrome:current that causes an error on
remote chrome standalone. If you need to run the remote docker selenium
standalone image do it on the 3.4 tag.

```bash
docker run -p 4444:4444 selenium/standalone-chrome:3.4
```

And this should work for Sauce Labs (Note that the parenthesis on SL_DC on
mandatory on this command when they're optional for the rest of example
variables.) You of course have to change the url where is says
*YOUR_SAUCE_USERNAME* and *YOUR_SAUCE_ACCESS_KEY* to credentials:

```bash
SELENIUM=http://YOUR_SAUCE_USERNAME:YOUR_SAUCE_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub SL_DC='{"platform": "Mac OS X 10.9", "browserName": "chrome", "version": "31"}'  DRIVER=saucelabs HOST_URL=https://bynd.com behave qa/functional/features
```

\* haven't tried sauce yet.


### Notes about example tests

* Useful documentation about selenium and webdriver can be found [here](http://selenium-python.readthedocs.io/) 
    (don't miss the webdriver part [here](http://selenium-python.readthedocs.io/api.html#locate-elements-by)) I find 
    the better than the [Selenium documentation](http://www.seleniumhq.org/docs/) but you should
    check that out as well. For Behave I suggest 
    [behave integration](http://behave.readthedocs.io/en/latest/tutorial.html),
    [behave features](https://pythonhosted.org/behave/gherkin.html#given-when-then-and-but), and beware they hide 
    really important stuff in the appendix.
* On Mac if keep Python Permission prompts when you launch Chromedriver, 
    follow these [instructions](http://bd808.com/blog/2013/10/21/creating-a-self-signed-code-certificate-for-xcode/) to 
    create a certificate. Run `. env/bin/activate` once and then stop it to get in the virtual env. It should now 
    say `(env)` on Terminal command line, then run this command, replacing *NAME* with the name of the certificate 
    you created.
    
    ```bash
    codesign -s NAME -f `which python`
    ```
    
* Note, if you keep this for a while and keep updating your local browser eventually the browser may no longer work 
    with the chromedriver you originally installed. You can update them with.
    
    ```bash
    . qa/utilities/driver_update/geckodriver.sh
    . qa/utilities/driver_update/chromedriver.sh
    ```
    
* I can't promise I will keep it up to date but I have a login to Google Behave Step in `qa/functional/steps/login` 
    that mimicks a human login. It is dependent on setting up environmental variables. pass in the name of the account, 
    e.g. `editor`. You then need to import the step into the tests named stepfile or common, 
    e.g. `from qa.functional.features.steps.login import LoginPage`. But the IAP setup mentioned in the main readme 
    is definitely a better option if you are using chrome and chrome emulator only.
* HTML should be validated to make sure it functions. I have an [example using python](https://github.com/Jiff21/Notes/blob/master/test/behave/features/steps/best_practices.py), 
    but this should ideally be done with a [gulp](https://www.npmjs.com/package/gulp-html-validator) or [grunt](https://www.npmjs.com/package/grunt-html-validation) task.
* If you want to use a Selenium Grid, like `headless_chrome` browser.py option uses, you need to also copy down 
    selenium and run a hub and a node before running the test:


#### Install

```bash
curl -L https://goo.gl/hvDPsK --output qa/env/bin/selenium.jar
```

#### Run

Start a hub:

```bash
java -Dwebdriver.chrome.driver=qa/env/bin/chromedriver -jar qa/env/bin/selenium.jar  -role hub
```

Start a Node based on the config file:

```bash
java -Dwebdriver.chrome.driver=qa/env/bin/chromedriver -jar qa/env/bin/selenium.jar  -role node -nodeConfig qa/utilities/selenium/nodeconfig.json
```

Optionally, you can do some conifguration of a node on command line instead of previous command:

```bash
java -Dwebdriver.chrome.driver=qa/env/bin/chromedriver -jar qa/env/bin/selenium.jar  -role  node -hub http://localhost:4444/grid/register -port 5556  -browser browserName=firefox,javascriptEnabled=true,maxInstances=10,platform=ANY -browser browserName=chrome,javascriptEnabled=true,maxInstances=10,platform=ANY -browser browserName=safari,javascriptEnabled=true,maxInstances=1,platform=ANY
```

Notes:
* Chrome Headless does not support extensions.
* set_network_conditions is local only for now, need to look into https://github.com/SeleniumHQ/selenium/issues/6217
