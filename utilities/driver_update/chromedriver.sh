#!/bin/bash

LATEST_CHROMEDRIVER=$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE)

echo 'Downloading Chromedriver ' $LATEST_CHROMEDRIVER
if [ "$(uname)" == "Darwin" ]; then
  echo 'on OSX 64'
  curl -L https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER/chromedriver_mac64.zip >> chromedriver.zip
  unzip chromedriver.zip
  mv chromedriver qa/env/bin/chromedriver
  rm chromedriver.zip
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  echo 'on Linux 64'
  curl -L https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER/chromedriver_linux64.zip >> chromedriver.zip
  unzip chromedriver.zip
  mv chromedriver /usr/bin/chromedriver
  rm chromedriver.zip
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  echo 'on Windows 32'
  curl -L https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER/chromedriver_win32.zip >> chromedriver.zip
  unzip chromedriver.zip
  mv chromedriver /usr/bin/chromedriver
  rm chromedriver.zip
fi
