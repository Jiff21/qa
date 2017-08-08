import os
import time
import json
from pprint import pprint
from zapv2 import ZAPv2
from qa.environment_variables import BASE_URL, ZAP_ADDRESS, ZAP_API_KEY
from qa.environment_variables import QA_FOLDER_PATH
# Connect to Zap instance
zap = ZAPv2(apikey=ZAP_API_KEY, proxies={
            'http': ZAP_ADDRESS, 'https': ZAP_ADDRESS})

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
pprint(zap.core.alerts())

alerts_json = json.dumps(zap.core.alerts())
write_path = '%s/security/results.json' % QA_FOLDER_PATH
alerts_file = open(write_path, 'w')
alerts_file.write(str(alerts_json))
alerts_file.close()
