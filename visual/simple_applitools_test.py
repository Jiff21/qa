from selenium import webdriver
from applitools.eyes import Eyes
from qa.accounts import EYES_API_KEY
from selenium.webdriver.chrome.options import Options


class HelloWorld:

    eyes = Eyes()

    eyes.api_key = EYES_API_KEY

    try:
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        eyes.open(driver=driver, app_name='New App', test_name='New Test',
                  viewport_size={'width': 800, 'height': 600})
        driver.get(r'https://google.com/about')
        eyes.check_window('New Test!')
        eyes.close()

    finally:
        driver.quit()
        eyes.abort_if_not_closed()
