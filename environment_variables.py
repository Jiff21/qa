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
