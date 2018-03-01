#!/bin/bash

LATEST_CHROMEDRIVER=$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
curl -L https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER/chromedriver_mac64.zip | tar xz -C qa/env/bin
