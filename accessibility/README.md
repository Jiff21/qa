# Accessibility

## Introduction

Test written using [Behave Framework](http://pythonhosted.org/behave/) and
[Lighthouse](https://github.com/GoogleChrome/lighthouse)

## Dependancies
Local node above 10 is necessary. I suggest using NVM.


## Install

*(if you didn't install as part of main README.MD)*

Install [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac) if not
already installed.

```bash
docker pull jiffcampbell/lighthouse:0.2
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
`PAGES_DICT` from `qa/settings.py`. `HOST_URL` is optional but without
it will run locally. See below for individual run commands. In another tab run
`docker run -p 8085:8085 jiffcampbell/lighthouse`

Scan all the pages from  the pages dict minus excluded pages in the
`LIGHTHOUSE_SKIPS` list found in `qa/settings`.

```bash
source qa/env/bin/activate
HOST=google.com python3 qa/accessibility/lighthouse_scan_runner.py
behave qa/accessibility/features
```

You can scan a single url with the following command.
```bash
SINGLE_LH_URI='/example/uri' SINGLE_LH_PAGE_NAME='test page' python3 qa/accessibility/lighthouse_scan_runner.py

```

Then you could run only assertions against the test page by adding a separate
Example to the necessary tests.

```
    @example_tag
    Examples: example of something that's failing.
      | page                 | format |
      | products page        |  json  |
```

And then trigger the bash tests

```bash
behave qa/accessibility/features -t '@example_tag'
```


### Dependancies

The PAGES_DICT in qa/settings contains valid URLs for the domain.

• When searching through large json, use
  [json-path finder](https://atom.io/packages/json-path-finder) from Atoms cmd + shift + p
  menu (after installing package)
