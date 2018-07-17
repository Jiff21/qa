#!/bin/bash

GECKODRIVER_REDIRECT=$(curl https://github.com/mozilla/geckodriver/releases/latest)

if [[ $GECKODRIVER_REDIRECT =~ v([[:digit:]]+\.[[:digit:]]+\.[[:digit:]]+)\"\> ]];
then
  LATEST_GECKODRIVER=${BASH_REMATCH[1]}
fi

echo 'Downloading Geckodriver ' $LATEST_GECKODRIVER
curl -L https://github.com/mozilla/geckodriver/releases/download/v$LATEST_GECKODRIVER/geckodriver-v$LATEST_GECKODRIVER-macos.tar.gz | tar xz -C qa/env/bin
