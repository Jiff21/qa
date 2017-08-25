# Visual

## Introduction
[Applitools](https://applitools.com/) is a visual regression testing tool.

## Install
*(if you didn't use main setup.sh script)*
```
source qa/env/bin/activate
pip install -r qa/visual/requirements.txt
```
Applitools offers a [free trial](https://applitools.com/users/register) (and a [free tier](https://applitools.com/pricing) that will run 25 validations a week). Go and sign up so you have a key to run tests.

## Running Tests

Simply run:
```
EYES_API_KEY='0123456789' behave qa/visual/features
```

You also have the option of changing the URL
```
BASE_URL=https://pythonhosted.org behave qa/visual/features/
```


### Notes

* You can also run applitools (locally)[http://support.applitools.com/customer/portal/articles/2285997]


In my experience so far (webdrivercss & phantomcss) the issue with these tools is flakyness of of the visual difference testing, Applitools is likely worth paying for [Match Level](https://applitools.atlassian.net/wiki/spaces/Java/pages/1540306/Selenium+-+Python#Selenium-Python-N) (Smart exclusion on content changes) alone. Here are some alternatives if you don't want to pay:
  * [dpxdt](https://github.com/bslatkin/dpxdt)
  * [webdrivercss](https://hub.docker.com/r/grugnog/webdrivercss/)
  * [Galen](http://galenframework.com/)
  * [Python + Needle](http://the-creative-tester.github.io/Python-Visual-Regression-Testing/)

* Their example of an [ignore](https://github.com/applitools/eyes.selenium.python/blob/master/samples/test_script.py) but they currently have a bug on Retina displays that makes this worthless. It's fixed in Java version but they have not fixed it in
