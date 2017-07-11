import os
import time
from pprint import pprint
from zapv2 import ZAPv2
from accounts import Accounts
from environment_variables import BASE_URL

BASE_URL = os.getenv('BASE_URL', BASE_URL)
ZAP_SERVER_PROXY = os.getenv(
    'ZAP_SERVER_PROXY',
    Accounts.ZAP_API_IP + ':' + Accounts.ZAP_API_PORT
)
API_KEY = Accounts.ZAP_API_KEY

zap = ZAPv2(
    apikey=API_KEY,
    proxies={
        'http': "http://%s" % ZAP_SERVER_PROXY,
        'https': "https://%s" % ZAP_SERVER_PROXY
    }
)

# Proxy a request to the target so that ZAP has something to deal with
print('Accessing target {}'.format(BASE_URL))
zap.urlopen(BASE_URL)
# Give the sites tree a chance to get updated
time.sleep(2)

print('Spidering target {}'.format(BASE_URL))
scanid = zap.spider.scan(BASE_URL)
# Give the Spider a chance to start
time.sleep(2)
while (int(zap.spider.status(scanid)) < 100):
    # Loop until the spider has finished
    print('Spider progress %: {}'.format(zap.spider.status(scanid)))
    time.sleep(2)

print ('Spider completed')

while (int(zap.pscan.records_to_scan) > 0):
    print ('Records to passive scan : {}'.format(zap.pscan.records_to_scan))
    time.sleep(2)

print ('Passive Scan completed')

print ('Active Scanning target {}'.format(BASE_URL))
scanid = zap.ascan.scan(BASE_URL)
while (int(zap.ascan.status(scanid)) < 100):
    # Loop until the scanner has finished
    print ('Scan progress %: {}'.format(zap.ascan.status(scanid)))
    time.sleep(5)

print ('Active Scan completed')

# Report the results

print ('Hosts: {}'.format(', '.join(zap.core.hosts)))
print ('Alerts: ')
zap.core.alerts()

f = open('pen/results.json', 'w')
f.write(str(zap.core.alerts()))
f.close()
