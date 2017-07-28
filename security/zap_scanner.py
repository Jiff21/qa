import os
from qa.accounts import ZAP_API_IP, ZAP_API_KEY,  ZAP_API_PORT
from qa.environment_variables import BASE_URL
from qa.security.scanner import Scanner


scanner = Scanner()
ZAP_SERVER_PROXY = os.getenv('ZAP_SERVER_PROXY', ZAP_API_IP + ':' + ZAP_API_PORT)
scanner.run(BASE_URL, ZAP_SERVER_PROXY, ZAP_API_KEY)
