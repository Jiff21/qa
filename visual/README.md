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

Note: You can also run applitools (locally)[http://support.applitools.com/customer/portal/articles/2285997]


In my experience so far (webdrivercss & phantomcss) the issue with these tools is flakyness of of the visual difference testing, Applitools is likely worth paying for.  Hut are some alternatives if you don't want to pay:
• [dpxdt](https://github.com/bslatkin/dpxdt)
• [webdrivercss](https://hub.docker.com/r/grugnog/webdrivercss/)
• [Galen](http://galenframework.com/)
• [Python + Needle](http://the-creative-tester.github.io/Python-Visual-Regression-Testing/)
