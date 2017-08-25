# Performance

## Introduction
[Locust](http://locust.io/) is a performance testing framework written in human readable code, that supports running load tests distributed over multiple machines.

## Installation
*(if you didn't use main setup.sh script)*
Install pip, virtualenv, & libevent if not already installed.
```
sudo easy_install pip
pip install virtualenv
brew install libevent
```
Create a new virtualbox, this one running in 2.7 as locust.io only supports to 3.4 (06/2017)
```
virtualenv --python=/usr/bin/python2.7 qa/pytwo_env
```
Install dependancies while in the virtualenv
```
source qa/pytwo_env/bin/activate
pip install -U -r qa/performance/requirements.txt
```

## Running Tests
In pytwo_env, run [Locust.io](http://docs.locust.io/en/latest/quickstart.html) with the following command:
```
locust -f qa/performance/locustfile.py --host=https://example.com
```
After that command go to the web interface [http://0.0.0.0:8089/](http://0.0.0.0:8089/). Where you can start a test, but once again **DO NOT RUN TEST WITH MORE THAN A COUPLE USERS** or really run this too frequently if you're pointed at **bynd.com** as you risk bringing our site down, running up hosting fees or throwing off analytics.

You can also launch it from the command line. *--num-request* or *-n* is used to shutdown after a certain number or requests.
```
locust --clients=2 --hatch-rate=1 --num-request=4 --no-web -f qa/performance/locustfile.py --host=https://google.com
```

More run commands in  [documentation](http://docs.locust.io/en/latest/quickstart.html#start-locust) so you can look there for running a multi-process file. Or check `locust -h` for other commands like how to put the output in a file that you could use to email someone as part of CI.
