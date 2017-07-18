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

May switch to:
```
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t https://www.example.com -n qa/pen/custom.conf -r qa/pen/testreport.html -z '-config scanner.strength=INSANE'
```
But not reading config. See https://github.com/zaproxy/zaproxy/wiki/ZAP-Baseline-Scan for progress file flag as well.

Or maybe:
https://github.com/Grunny/zap-cli but this is a 3.6 issue (https://github.com/zaproxy/zap-api-python/pull/4 / https://github.com/zaproxy/zaproxy/issues/2308 / both closed but a know issue (https://groups.google.com/forum/#!msg/zaproxy-users/pWaukbxtG-M/mrUzGn-aBgAJ)
```
ZAP_PATH='qa/env/bin/ZAP_2.6.0/zap-2.6.0.jar' zap-cli start --start-options "-config api.key=0123456789'
docker run -i owasp/zap2docker-stable zap-cli quick-scan --self-contained -o "-config api.key=0123456789 -config scanner.strength=INSANE -config scanner.strength=HIGH" https://example.com
```
Might need ```curl -L https://github.com/zaproxy/zaproxy/releases/download/2.6.0/ZAP_2.6.0_Core.tar.gz | tar xz -C qa/env/bin``` then ```ZAP_PATH=$PWD/qa/env/bin/ZAP_2.6.0/ zap-cli start --zap-url 0.0.0.0  --start-options "-config api.key=0123456789"``` and then  ```  ZAP_PATH=$PWD/qa/env/bin/ZAP_2.6.0/ zap-cli --api-key 0123456789 quick-scan --self-contained -o '-config api.key=0123456789' -s spider,xss,active-scan http:/google.com```

### Notes

While the docker session is running you can access settings at [http://0.0.0.0:8090/UI/core](http://0.0.0.0:8090/UI/core)
