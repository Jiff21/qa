# Allure

## Introduction

Allure is amalgamates test results in a readable report. It gives you pretty
graphs, a historical timeline and can group tests by severity or features.


## Install

Create a virtualenv if not already.

```bash
virtualenv -p python3 qa/env
```

Install allure

```bash
brew install allure
source env/bin/activate
pip3 install -r qa/utilities/allure/requirements.txt
```


## Running tests

Run requite commands from accessibility and security to generate json report data.

```bash
brew install allure
```

Run all the commands inside of virtualenv where allure-behave was installed
(e.g. `. qa/env/bin/activate`) Generate an allure formatted report for each
section

Accessibility:

```bash
BASE_URL=https://google.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results ./qa/accessibility/features
```

Functional:

```bash
BASE_URL=https://google.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results ./qa/functional/features
```

Analytics:

```bash
DRIVER=ga_chrome BASE_URL=https://www.google.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results ./qa/analytics/features
```

Security:

```bash
BASE_URL=https://example.com behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results ./qa/security/features
```

Visual:
After running firefox and chrome visual tests.

```bash
behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results/ qa/visual/features/ --no-skipped
```

Performance:
After running locust tests separately.

```bash
behave -f allure_behave.formatter:AllureFormatter -o qa/utilities/allure/allure_results/ qa/performance/features/ --no-skipped
```


## Reports

It's best to make & serve results using:

```bash
allure generate qa/utilities/allure/allure_results/ -o qa/utilities/allure/allure-reports/ --clean
allure open qa/utilities/allure/allure-reports/
```

If you want a History section, you need to copy the history from the previous
report, before generating the next report.

```bash
cp -R qa/utilities/allure/allure-reports/history/ qa/utilities/allure/allure_results/history
```

You can do it in one step like this, but has downsides.

```bash
allure serve qa/utilities/allure/allure_results
```

If you are hosting your allure reports on a server. The report exporter can send
them to it. The uncommented out code if for use with Google IAP on. If the
report hub is unsecured or your hosting locally, use the commented out code.

In my case it's using IAP so you have to also install.

```bash
pip3 install -r qa/utilities/oauth/requirements.txt
```

Then you can upload with this

```bash
GOOGLE_APPLICATION_CREDENTIALS=fake/path/to/service-account.json ALLURE_PROJECT_NAME=example ALLURE_HUB_CLIENT_ID=fake-##s-for-cloud-console-client-id.apps.googleusercontent.com  ALLURE_REPORT_HUB_URL=https://example/allure-hub.com python3 qa/utilities/allure/report_exporter.py
```


### Notes

If you can split up your tests per environment and browser you can send an
Environment file to the json folder before report generation.

```bash
echo -e "Browser=$DRIVER\nEnvironment=$ENVIRONMENT_NAME" > qa/utilities/allure/allure_results/environment.properties
```
