# Applitools

## Introduction
[Appitools](https://applitools.com/) is a visual regression testing tool.

## Install
*(if you didn't use main setup.sh script)*
```
source qa/env/bin/activate
pip install -r qa/visual/requirements.txt
```

## Running Tests

Simply run:
```
behave qa/visual/features
```

You also have the option of changing the URL
```
BASE_URL=https://pythonhosted.org behave qa/visual/features/
```


https://github.com/applitools/eyes.selenium.python
https://applitools.com/resources/tutorial/selenium/python#step-3


ALtern:
https://github.com/bslatkin/dpxdt
http://galenframework.com/
http://the-creative-tester.github.io/Python-Visual-Regression-Testing/
Or just see if appitools make webdrivercss assertions better. https://hub.docker.com/r/grugnog/webdrivercss/
If you stay with the applitools check out http://support.applitools.com/customer/portal/articles/2285997
