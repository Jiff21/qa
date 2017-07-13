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
Run the following command to generate an html and json report. These will generate reports based off the end of the path. So ```--output-path=/lighthouse/output/example``` will create a the following report /accessibility/output/example.report.json

```
docker run -v $PWD/accessibility/output/:/lighthouse/output/  -i matthiaswinkelmann/lighthouse-chromium-alpine http://probable-quest.appspot.com/ --output json --output html  --output-path=/lighthouse/output/example https://example.com
```
Then run behave assertions against them.
```
behave accessibility/features
```


Note;
• Look into this for CI could run it behind e2e test then use files:
https://sites.google.com/a/chromium.org/chromedriver/logging/performance-log

• When searching through large json, use json-path finder from Atoms cmd + shift + p menu (after installing package)
