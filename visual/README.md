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

## Running Tests

```
BASE_URL=http://testapp.galenframework.com galen test qa/visual/tests/ --htmlreport qa/visual/reports --config qa/visual/galen.config
```
