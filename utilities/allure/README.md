# Allure

## Introduction
Allure is amalgamates test results in a readable report. It gives you pretty graphs, a historical timeline and can group tests by severity or features.

## Install
Create a virtualenv if not already.
```
virtualenv -p python3 qa/env
```
Install allure
```
brew install allure
source env/bin/activate
pip3 install -r qa/utilities/allure/requirements.txt
```

## Running tests
Run requite commands from accessibility and security to generate json report data.
brew install allure
Run all the commands inside of virtualenv where allure-behave was installed(e.g. `. qa/env/bin/activate`)
Generate an allure formatted report for each section
Accessibility:
```
BASE_URL=https://google.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results ./qa/accessibility/features
```

Functional:
```
BASE_URL=https://google.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results ./qa/functional/features
```

Analytics:
```
DRIVER=ga_chrome BASE_URL=https://www.google.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results ./qa/analytics/features
```

Security:
```
BASE_URL=https://example.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results ./qa/security/features
```

Visual:
Not yet supported due to
```
```

Once all reports are generated you can serve them locally:
```
allure serve qa/utilities/allure/allure_results
```
