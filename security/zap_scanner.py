import os
from qa.security.scanner import Scanner
from qa.accounts import Accounts
from qa.environment_variables import BASE_URL


scanner = Scanner()
accounts = Accounts()
ZAP_SERVER_PROXY = os.getenv('ZAP_SERVER_PROXY', accounts.ZAP_API_IP + ':' + accounts.ZAP_API_PORT)
scanner.run(BASE_URL, ZAP_SERVER_PROXY, accounts.ZAP_API_KEY)
