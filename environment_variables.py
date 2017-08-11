import os

BASE_URL = os.getenv('BASE_URL', 'http://localhost:3000')
DRIVER = os.getenv('DRIVER', 'chrome')
DRIVER = DRIVER.lower().replace(' ', '_').replace('-', '_')
LIGHTHOUSE_IMAGE = os.getenv('LIGHTHOUSE_IMAGE', 'http://localhost:8080')
SELENIUM = os.getenv('SELENIUM', 'http://localhost:4444/wd/hub')
SL_DC = os.getenv(
    'SL_DC',
    '{"platform": "Mac OS X 10.9", "browserName": "chrome", "version": "31"}'
)
PAGES_LIST = ['/about', '/contact']
QA_FOLDER_PATH = os.getenv('QA_FOLDER_PATH', 'qa/')
DRIVER = os.getenv('DRIVER', 'chrome')
# Admin Email and password for CMS Testing
ADMIN_URL_DICT = {
    'https://example.com': 'https://example.com/admin-uri',
    'https://www.testing.appspot.com': 'https://www.testing.appspot.com/admin-uri',
    'https://www.dev.appspot.com': 'https://www.dev.appspot.com/admin-uri',
    'https://www.staging.appspot.com': 'https://ewww.staging.appspot.com/admin-uri'
}
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'byndtest11@gmail.com')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'fakepassword')
ADMIN_NAME = os.getenv('ADMIN_NAME', 'Al\' Admin')

EDITOR_EMAIL = os.getenv('EDITOR_EMAIL', 'fakeUser2@gmail.com')
EDITOR_PASSWORD = os.getenv('EDITOR_PASSWORD', 'fakepassword')
EDITOR_NAME = os.getenv('EDITOR_NAME', 'Eddie Editor')

USER_EMAIL = os.getenv('USER_EMAIL', 'fakeUser3@gmail.com')
USER_PASSWORD = os.getenv('USER_PASSWORD', 'fakepassword')
USER_NAME = os.getenv('USER_NAME', 'Vinny Testaverde')

RECOVERY_EMAIL = os.getenv('RECOVERY_EMAIL', 'another_fake_email@gmail.com')

ZAP_ADDRESS = os.getenv('ZAP_ADDRESS', 'http://localhost:8080')
ZAP_API_KEY = os.getenv('ZAP_API_KEY', '0123456789')

EYES_API_KEY = os.getenv('EYES_API_KEY', '0123456789')

# Google
CLIENT_ID = os.getenv(
    'CLIENT_ID', '012345678901-am29widj4kW0l57Kaqmsh3ncjskepsk2.apps.googleusercontent.co')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    'GOOGLE_APPLICATION_CREDENTIALS', '/path/to/json/web/token.json')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '0123456789')
