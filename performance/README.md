# Performance

## Introduction

[Locust](http://locust.io/) is a performance testing framework written in human readable code, 
that supports running load tests distributed over multiple machines.

## Installation

*(if you didn't install as part of main README.MD)*
Install pip, virtualenv, & libevent if not already installed.

```bash
sudo easy_install pip
pip install virtualenv
brew install libevent
```

Create a virtualenv if not already.

```bash
virtualenv -p python3 qa/env
```

Install dependancies while in the virtualenv

```bash
source qa/env/bin/activate
pip3 install -U -r qa/performance/requirements.txt
```

## Running Tests

In virtualenv, the following python script will trigger a locustio run and then run behave 
assertions against the resulting csv:

```bash
HOST_URL=https://google.com python3 qa/performance/runner.py
```

To change the number of clients, hatch-rate, or number of requests before shutting down 
change `--clients=3 --hatch-rate=1 --num-request=6` respectively in `qa/performance/runner.py`. If you want to change 
the time assertions, edit the then statements in `qa/performance/features/performance.feature`.

While debugging you can run locust from the command line. *--num-request* or *-n* is used to shutdown after a certain 
number or requests.

```bash
locust --clients=60 --hatch-rate=1 --num-request=200 --no-web --csv=qa/performance/results/ --host=https://google.com -f qa/performance/locustfile.py
```

More run commands in  [documentation](http://docs.locust.io/en/latest/quickstart.html#start-locust) so you can look 
there for running a multi-process file. Or check `locust -h` for other commands like how to put the output in a file 
that you could use to email someone as part of CI.

If you need to trigger a single run of behave assertions after generating a CSV file, run:

```bash
behave qa/performance/features
```

If you want to test through the locust web gui:

```bash
locust --host=https://google.com
```

After that command go to the web interface [http://0.0.0.0:8089/](http://0.0.0.0:8089/).
