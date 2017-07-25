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

<<<<<<< HEAD
https://github.com/zacharyvoase/pdiffer
=======
Note: You can also run applitools (locally)[http://support.applitools.com/customer/portal/articles/2285997]


In my experience so far (webdrivercss & phantomcss) the issue with these tools is flakyness of of the visual difference testing, Applitools is likely worth paying for.  Hut are some alternatives if you don't want to pay:
• [dpxdt](https://github.com/bslatkin/dpxdt)
• [webdrivercss](https://hub.docker.com/r/grugnog/webdrivercss/)
• [Galen](http://galenframework.com/)
• [Python + Needle](http://the-creative-tester.github.io/Python-Visual-Regression-Testing/)

**Tips**
Their example of an [ignore](https://github.com/applitools/eyes.selenium.python/blob/master/samples/test_script.py)
>>>>>>> master
