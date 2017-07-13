# Accessiblity

## Introduction

Test written using [Behave Framework](http://pythonhosted.org/behave/) and [Lighthouse](https://github.com/GoogleChrome/lighthouse)


## Install

Install [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac) if not already installed.
```
docker pull matthiaswinkelmann/lighthouse-chromium-alpine
```
Create a virtualenv if not already.
```
virtualenv -p python3 env
```
Install dependencies to virtualenv.
```
source env/bin/activate
pip3 install -r e2e/requirements.txt
```

# Run
This command will run against all pages the index page and all pages in PAGES_LIST from environment_variables.py. BASE_URL is optional but without it it will run locally. See below for individual run commands.
```
BASE_URL='https:/example.com' python accessibility/page_runner.py
```


To run lighthouse report generator. These will generate reports based off the end of the path. So ```--output-path=/lighthouse/output/example``` will create a report at ```accessibility/output/example.report.json```

```
docker run -v $PWD/accessibility/output/:/lighthouse/output/  -i matthiaswinkelmann/lighthouse-chromium-alpine --output json --output html  --output-path=/lighthouse/output/example https://example.com
```

Then run behave assertions against them, note example needs to match the name used for the end of the output path in the command below.
```
BASE_URL='https:/example.com' FILE_NAME=example behave accessibility/features
```

Note:
• Look into [this](https://sites.google.com/a/chromium.org/chromedriver/logging/performance-log) for CI could run it behind e2e test then use files:
• When searching through large json, use [json-path finder](https://atom.io/packages/json-path-finder) from Atoms cmd + shift + p menu (after installing package)
