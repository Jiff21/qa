# Accessibility

## Introduction

Test written using [Behave Framework](http://pythonhosted.org/behave/) and
[Lighthouse](https://github.com/GoogleChrome/lighthouse)


## Install

*(if you didn't install as part of main README.MD)*

Install [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac) if not
already installed.

```bash
docker pull kmturley/lighthouse-ci
```

Create a virtualenv if not already.

```bash
virtualenv -p python3 qa/env
```

Install dependencies to virtualenv.

```bash
source qa/env/bin/activate
pip3 install -U -r qa/accessibility/requirements.txt
```


## Running Tests

This command will run against all pages the index page and all pages in
`PAGES_DICT` from `qa/settings.py`. `BASE_URL` is optional but without
it will run locally. See below for individual run commands.

```bash
source qa/env/bin/activate
docker run -p 8085:8085 kmturley/lighthouse-ci
BASE_URL=https:/google.com python qa/accessibility/page_runner.py
```

To run lighthouse report generator. These will generate reports based off the end of the path. So ```--output-path=/lighthouse/output/about``` will create a report at ```accessibility/output/about.report.json```

```bash
docker run -p 8085:8085 kmturley/lighthouse-ci
BASE_URL=https:/google.com PAGE=/about python qa/accessibility/single_run.py
```

Then run behave assertions against them, note example needs to match the name used for the end of the output path in the command below.

```bash
BASE_URL=https:/google.com FILE_NAME=about behave qa/accessibility/features
```

If you need a more human readable file fun.

```bash
BASE_URL=https:/google.com FORMAT=html python qa/accessibility/single_run.py
```


### Dependancies

The PAGES_DICT in qa/settings contains valid URLs for the domain.

Note:

• Look into [this](https://sites.google.com/a/chromium.org/chromedriver/logging/performance-log)
  for CI could run it behind functional test then use files:

• When searching through large json, use
  [json-path finder](https://atom.io/packages/json-path-finder) from Atoms cmd + shift + p
  menu (after installing package)
