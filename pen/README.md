---
# Pen Tests
---

## Zap via Behave

### Installation
*(if you didn't use main setup.sh script)*
Install pip, virtualenv, & libevent if not already installed.
```
sudo easy_install pip
pip install virtualenv
```
Create a  virtualbox, if you haven't before
```
virtualenv -p python3 env
```
Install dependancies while in the virtualenv
```
source env/bin/activate
pip install -r qa/pen/requirements.txt
docker pull owasp/zap2docker-stable
```

### Running Tests
First start the docker machine with the api.key matching, -host matching ZAP_API_ADDRESS, and the ports matching ZAP_API_PORT from the qa.accounts.py.
The command should look something like this
```
docker run -p 8090:8090 -i owasp/zap2docker-stable zap.sh -daemon -port 8090 -host 0.0.0.0 -config api.key=0123456789 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true -config scanner.strength=INSANE
BASE_URL=https://example.com ZAP_SERVER_PROXY=0.0.0.0:8090 python qa/pen/zap_scanner.py
```

Run behave scenarios against scanner results:
```
behave qa/pen/features
```

If you're not running under default domain in environment_variables.py
```
BASE_URL=https://example.com  behave qa/pen/features
```

### Notes

While the docker session is running you can access settings at [http://0.0.0.0:8090/UI/core](http://0.0.0.0:8090/UI/core)
