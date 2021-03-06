# Security

## Zap via Behave

## Installation

*(if you didn't install as part of main README.MD)*
Install pip, virtualenv, & libevent if not already installed.

```bash
sudo easy_install pip
pip install virtualenv
```

Create a  virtualbox, if you haven't before

```bash
virtualenv -p python3 env
```

Install dependancies while in the virtualenv (pip dev version until [9.0.2 
released](https://github.com/pypa/pip/issues/4216))

```bash
source env/bin/activate
pip install -I https://github.com/pypa/pip/archive/master.zip#egg=pip
pip3 install -r -U qa/security/requirements.txt
docker pull owasp/zap2docker-stable
. qa/utilities/driver_update/chromedriver.sh
```

## Running Tests

First start the docker machine with the api.key matching, 
-host `ZAP_API_ADDRESS` and `ZAP_API_KEY` and the ports set in the 
`qa/settings.py` or passed in from the command line.

The command should look something like this

```bash
docker run -p 8081:8081 -i owasp/zap2docker-stable zap.sh -daemon -port 8081 -host 0.0.0.0 -config api.key=0123456789 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true -config scanner.strength=INSANE
```

Then run a scan:

```bash
HOST_URL=https://example.com ZAP_ADDRESS=0.0.0.0:8081 ZAP_API_KEY=0123456789 python qa/security/zap_scanner.py
```

Run behave scenarios against scanner results:

```bash
behave qa/security/features
```

If you're not running under default domain in qa/settings.py

```bash
HOST_URL=https://example.com behave qa/security/features
```


### Notes

* While the docker session is running you can access settings at 
  [http://0.0.0.0:8081/UI/core](http://0.0.0.0:8081/UI/core)
* I removed zapcli==0.9.0 from requirements as I'm not using it. But if we need 
  to use zapcli, we need to sandbox it in virtualenv for Dockerfile and 
  docker-compose as it conflicts with locust.
