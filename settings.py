import logging
import os
from dotenv import load_dotenv

logging.basicConfig()
log = logging.getLogger('BYNDQA')
log.setLevel(os.getenv('LOG_LEVEL', 'ERROR'))

# use `export QA_ENV=name` to set the current envionrment you're testing against
QA_ENV = os.getenv('QA_ENV', 'local').lower()
if 'test' in QA_ENV:
    print('Loading Testing Environment variables')
    load_dotenv(dotenv_path='./qa/secrets/testing.env', verbose=True)
    IAP_ON = bool(os.getenv('IAP_ON', True))
elif 'dev' in QA_ENV:
    print('Loading Dev Environment variables')
    load_dotenv(dotenv_path='./qa/secrets/dev.env')
    IAP_ON = bool(os.getenv('IAP_ON', True))
elif 'stag' in QA_ENV:
    print('Loading Staging Environment variables')
    load_dotenv(dotenv_path='./qa/secrets/staging.env')
    IAP_ON = bool(os.getenv('IAP_ON', True))
elif 'production' in QA_ENV or 'live' in QA_ENV:
    print('Loading Production Environment variables')
    load_dotenv(dotenv_path='./qa/secrets/production.env')
    IAP_ON = bool(os.getenv('IAP_ON', False))
else:
    assert QA_ENV == 'local', 'Unrecognized ENV name'
    IAP_ON = bool(os.getenv('IAP_ON', False))
    print('Using default Environment variables')


########
# Overwritten by ENV files
########


# Host of server
HOST = os.getenv('HOST', 'localhost')
PORT = os.getenv('PORT', '3000')
# if 'local' in QA_ENV:
#     HOST_URL = os.getenv('HOST_URL', 'http://%s:%s' % (HOST, PORT))
# else:
HOST_URL = os.getenv('HOST_URL', 'https://%s' % HOST)

# Basic Auth
BASIC_AUTH_USER = os.getenv('BASIC_AUTH_USER', None)
BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD', None)

# Google IAP
CLIENT_ID = os.getenv(
    'CLIENT_ID', '012345678901-am29widj4kW0l57Kaqmsh3ncjskepsk2.apps.googleusercontent.co')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    'GOOGLE_APPLICATION_CREDENTIALS', '/path/to/json/web/token.json')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '0123456789')

# If you need firebase auth
FIREBASE_KEY = os.getenv('FIREBASE_KEY', 'sdhafhdasgahadghgdgha')

# Allure Report Hub
ALLURE_REPORT_HUB_URL=os.getenv('ALLURE_REPORT_HUB_URL', 'http://0.0.0.0:5000')
ALLURE_PROJECT_NAME=os.getenv('ALLURE_PROJECT_NAME', 'example')
ALLURE_HUB_CLIENT_ID=os.getenv('ALLURE_HUB_CLIENT_ID', 'example')

# Admin Email and password for CMS Testing
ADMIN_URL = 'https://example.com/admin-uri'

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'fakeUser1@gmail.com')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'fakepassword')
ADMIN_NAME = os.getenv('ADMIN_NAME', 'Al\' Admin')

EDITOR_EMAIL = os.getenv('EDITOR_EMAIL', 'fakeUser2@gmail.com')
EDITOR_PASSWORD = os.getenv('EDITOR_PASSWORD', 'fakepassword')
EDITOR_NAME = os.getenv('EDITOR_NAME', 'Eddie Editor')

USER_EMAIL = os.getenv('USER_EMAIL', 'fakeUser3@gmail.com')
USER_PASSWORD = os.getenv('USER_PASSWORD', 'fakepassword')
USER_NAME = os.getenv('USER_NAME', 'Vinny Testaverde')

NO_ACCESS_EMAIL = os.getenv('NO_ACCESS_EMAIL', 'fakeUser4@gmail.com')
NO_ACCESS_PASSWORD = os.getenv('NO_ACCESS_PASSWORD', 'fakepassword')

RECOVERY_EMAIL = os.getenv('RECOVERY_EMAIL', 'another_fake_email@gmail.com')
RECOVERY_CITY = os.getenv('RECOVERY_CITY', 'New New York')
RECOVERY_PHONE = os.getenv('RECOVERY_PHONE', '555-555-5555')

ZAP_ADDRESS = os.getenv('ZAP_ADDRESS', 'http://localhost:8080')
ZAP_API_KEY = os.getenv('ZAP_API_KEY', '0123456789')

EYES_API_KEY = os.getenv('EYES_API_KEY', '0123456789')

#########


ACCOUNTS = {
    'admin': {
        'email': ADMIN_EMAIL,
        'password': ADMIN_PASSWORD,
        'name': ADMIN_NAME
    },
    'editor': {
        'email': EDITOR_EMAIL,
        'password': EDITOR_PASSWORD,
        'name': EDITOR_NAME
    },
    'user': {
        'email': USER_EMAIL,
        'password': USER_PASSWORD,
        'name': USER_NAME
    },
    'no access user': {
        'email': NO_ACCESS_EMAIL,
        'password': NO_ACCESS_PASSWORD,
        'name': 'No access user'
    }
}



DRIVER = os.getenv('DRIVER', 'chrome')
DRIVER = DRIVER.lower().replace(' ', '_').replace('-', '_')
LIGHTHOUSE_IMAGE = os.getenv('LIGHTHOUSE_IMAGE', 'http://localhost:8085')
SELENIUM = os.getenv('SELENIUM', 'http://localhost:4444/wd/hub')
APPIUM_HUB = os.getenv('APPIUM_HUB', 'http://localhost:4723/wd/hub')
QA_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
QA_FOLDER_PATH = os.getenv('QA_FOLDER_PATH', 'qa/')

SL_DC = os.getenv(
    'SL_DC',
    '{"platform": "Mac OS X 10.9", "browserName": "chrome", "version": "31"}'
)

PAGES_DICT = {
    'index': '',
    'about':'/about',
    'products page':'/about/products',
    'contact':'/contact'
}
LIGHTHOUSE_SKIPS = ['contact']


DEFAULT_WIDTH = 1366
DEFAULT_HEIGHT = 768
MOBILE_WIDTH = 360
MOBILE_HEIGHT = 640
TABLET_WIDTH = 600
TABLET_HEIGHT = 1024


# Safari requires you account for OSX Top Nav & is iffy about edge
DEFAULT_BROWSER_POSITION = {
    'x': 10,
    'y': 30
}

PROXY_PASSTHROUGH = os.getenv('PROXY_PASSTHROUGH', [
    'example.storage.googleapis.com',
])

SLACK_URL = os.getenv('SLACK_URL', 'https://hooks.slack.com/services/blarg/blerg')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL', None)

OK_SRCS = [
    HOST_URL,
    '3p.ampproject.net',
    'abc.xyz',
    'ajax.googleapis.com',
    'cdn.firebase.com',
    'doubleclick.net',
    'fonts.googleapis.com',
    'gmodules.com',
    'google-analytics.com',
    'google.com',
    'google.[ccTLD]',
    'googleadservices.com',
    'googlegoro.com',
    'googleplex.com',
    'googletagmanager.com',
    'gstatic.com',
    'gstatic.cn',
    'imasdk.googleapis.com',
    'maps.googleapis.com',
    'oauth.googleusercontent.com',
    'pagead2.googlesyndication.com'
    's0.2mdn.net',
    'schema.org',
    'static.dialogflow.com',
    'tensorflow.org',
    'thinkwithgoogle.com',
    'www.googletagservices.com',
    'www.zagat.com',
    'youtube.com',
    'ytimg.com'
]

default_headers = {
    'Accept-Charset': 'UTF-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml,application/json,image/webp,image/apng,',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36, QA Tests'
}

print('QA_ENV is set to {}'.format(QA_ENV))
print('DRIVER is set to {}'.format(DRIVER))
print('HOST is set to {}'.format(HOST))
print('HOST URL is set to {}'.format(HOST_URL))
print('Proxy passthrough set to {}'.format(PROXY_PASSTHROUGH))
