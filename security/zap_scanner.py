from qa.security.scanner import Scanner
from qa.accounts import Accounts

scanner = Scanner()
accounts = Accounts()
scanner.run('http://' + accounts.ZAP_API_IP + ':' + accounts.ZAP_API_PORT, accounts.ZAP_API_KEY)
