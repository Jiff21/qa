# Visual

## Introduction
[Galen](http://galenframework.com/) is layout and functional testing framework.

## Install
*(if you didn't use main setup.sh script)*
```
source qa/env/bin/activate
pip3 install -U -r qa/visual/requirements.txt
curl -L https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-macos.tar.gz | tar xz -C qa/env/bin
. qa/utilities/driver_update/chromedriver.sh
curl -L https://github.com/galenframework/galen/releases/download/galen-2.3.6/galen-bin-2.3.6.zip | tar xy -C qa/env/bin
cd qa/env/bin/galen-bin-2.3.6 && sudo ./install.sh
```
Look into npm install instead maybe?
`npm install -g galenframework-cli`


## Running Tests

Run all tests:
```
galen test qa/visual/tests/  --config qa/visual/galen.config
```

Run a test:
```
galen test qa/visual/tests/browser.test  --config qa/visual/galen.config
```

Or Debug a gspec file width
```
galen check qa/visual/tests/specs/homepage.spec  --url http://samples.galenframework.com/tutorial1/tutorial1.html  --size 640x480  --config qa/visual/galen.config
```

You also have the option of changing the URL
```

```


### Notes
In my experience so far (webdrivercss, phantomcss, applitools) the issue with these tools is flakyness of of the visual difference:
  * [dpxdt](https://github.com/bslatkin/dpxdt)
  * [Python + Needle](http://the-creative-tester.github.io/Python-Visual-Regression-Testing/)
  * [Applitools](https://applitools.com/) [Match Level](https://applitools.atlassian.net/wiki/spaces/Java/pages/1540306/Selenium+-+Python#Selenium-Python-N) is promising (It was still a bit flaky when I tested it) but Applitools is priced per screenshot comparison hurts when you start doing 3 responsive sizes and say average 3 interactions per page, and want to test at 3 sizes. Suddenly you have to multiply every page you want to test by 9. Then if you're running per commit or say even just once a day you end up with math like (10 pages X 3 Sizes X 3 Interactions X 30.5 days = 2745 tests per months and that's above their $299 pro tier, you're looking at ~$750 worth of tests. And that's for 1 browser, double it for 2. If you want this to be fully worth it you'd probably want to start mixing in a range of browsers, interactions and device strings that would really mess this all up)
  * [percy](https://percy.io) is similar to applitools but  
  * [webdrivercss](https://github.com/webdriverio/webdrivercss) is free and allows you to test with chrome but it isn't being maintained and relies on webdriverio 2.0
  * phantomcss often misrenders things, can't test in actual browser, and is very flaky
