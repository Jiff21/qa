# Applitools

## Introduction
[Appitools](https://applitools.com/) is a visual regression testing tool.

## Install
*(if you didn't use main setup.sh script)*
```
source qa/locust_env/bin/activate
curl -L https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip | tar xz -C qa/locust_env/bi
pip install -r qa/visual/requirements.txt
```

## Running Tests

```
BASE_URL=https://pythonhosted.org REBASE=True behave qa/visual/features/ -i test
```

```
BASE_URL=https://pythonhosted.org behave qa/visual/features/ -i test
```

https://github.com/zacharyvoase/pdiffer
