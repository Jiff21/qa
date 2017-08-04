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
