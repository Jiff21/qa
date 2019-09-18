# Visual


## Introduction

[Galen](http://galenframework.com/) is layout and functional testing framework.


## Install

*(if you didn't install as part of main README.MD)*

```bash
source qa/env/bin/activate
pip3 install -U -r qa/visual/requirements.txt
. qa/utilities/driver_update/geckodriver.sh
. qa/utilities/driver_update/chromedriver.sh
curl -L https://github.com/galenframework/galen/releases/download/galen-2.3.6/galen-bin-2.3.6.zip | tar xy -C qa/env/bin/
cd qa/env/bin/galen-bin-2.3.6 && sudo ./install.sh && cd ../../../../
```


## Running Tests

Activate the virtualenv using ```. qa/env/bin/activate```

Run all galen test files:

```bash
HOST_URL=http://testapp.galenframework.com galen test qa/visual/tests/ --htmlreport qa/visual/reports --config qa/visual/galen.config
```

Run a test:

```bash
HOST_URL=http://testapp.galenframework.com galen test qa/visual/tests/homepage.test.js --htmlreport qa/visual/reports --config qa/visual/galen.config
```

Or Debug a gspec file width:

```bash
galen check qa/visual/specs/homepage.gspec  --url http://testapp.galenframework.com/  --size 640x1080  --config qa/visual/galen.config --include tablet
```

Or switch the browser with `DRIVER`:

```bash
DRIVER=firefox HOST_URL=http://testapp.galenframework.com galen test qa/visual/tests/ --htmlreport qa/visual/reports --config qa/visual/galen.config
```

Run Assertions against the results for galen tests.

```bash
behave qa/visual/features -t "~pillow"
```

Run all tests galen tests and trigger the behave assertions in 1 command

```bash
. qa/visual/run.sh http://testapp.galenframework.com
```


## Visual Diff Test Using Python Pillow

### Introduction

Screenshot comparison tests are also an option using python pillow. But they tend to be flaky unless you are  loading the page with mock data, and care about single pixel differences.  

### Run

If you need to you can update images using the REBASE=True option. You should do this 1 test at a time using the `-n` flag so you only update tests that should be updated as others may have bugs currently and you don't want to update those. Run without the -N once the first time after clone.

```bash
HOST=google.com REBASE=True behave qa/visual/features/ -n 'example test name'
HOST=google.com REBASE=True  DRIVER=firefox behave qa/visual/features/ -n 'example test name'
```

To run all tests.

```bash
HOST=google.com behave qa/visual/features/ -t pillow
HOST=google.com DRIVER=firefox behave qa/visual/features/ -t pillow
```


### Notes

In my experience so far (webdrivercss, phantomcss, applitools) the issue with these tools is flakyness of
the visual difference:

  * [dpxdt](https://github.com/bslatkin/dpxdt)
  * [Python + Needle](http://the-creative-tester.github.io/Python-Visual-Regression-Testing/)
  * [Applitools](https://applitools.com/)
    [Match Level](https://applitools.atlassian.net/wiki/spaces/Java/pages/1540306/Selenium+-+Python#Selenium-Python-N)
    is promising (It was still a bit flaky when I tested it) but Applitools is priced per screenshot
    comparison hurts when you start doing 3 responsive sizes and say average 3 interactions per page,
    and want to test at 3 sizes. Suddenly you have to multiply every page you want to test by 9.
    Then if you're running per commit or say even just once a day you end up with math like (10 pages X 3
    Sizes X 3 Interactions X 30.5 days = 2745 tests per months and that's above their $299 pro tier, you're
    looking at ~$750 worth of tests. And that's for 1 browser, what if you have a matrix of 5 or 10? It's
    too expensive.
  * [percy](https://percy.io) more reasonable pricing that applitools but lack layout comparison that made applitools more exciting than free options like webdrivercss.
  * [webdrivercss](https://github.com/webdriverio/webdrivercss) is free and allows you to test with chrome but it isn't being maintained and relies on webdriverio 2.0
  * phantomcss often renders things incorrectly, can't test in browser's actual user's use, and is very flaky
