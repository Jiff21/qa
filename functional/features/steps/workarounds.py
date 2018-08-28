import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

def scroll_to_webelement(driver, web_element):
    '''
    actions.move_to_element will fail in firefox if you do not scroll
    the element on screen beforehand.
    '''
    if 'firefox' in driver.capabilities['browserName'] \
        or 'safari' in driver.capabilities['browserName']:
        x = web_element.location['x']
        y = web_element.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        driver.execute_script(scroll_by_coord)
        driver.execute_script(scroll_nav_out_of_way)
