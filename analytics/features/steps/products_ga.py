'''
  Scenario: The Homepage fires an event when it loads
  Given I am on '/about/products/'
    When I check logs
    Then I should see "title" with a value of "Our Products | Google"

  Scenario: When I click a Products Learn More it should fire correct events
    Given I am on "/about/products/"
    When I click Youtube's Get Started button
      And I click Youtube's Learn more
      And I check logs
    Then I should see "eventLabel" with a value of "YouTube:Learn more"
      And I should see "eventCategory" with a value of "Module:Product Link List"
      And I should see "eventAction" with a value of "watch, listen, and play: youtube"

'''
import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.analytics.features.steps.common import CommonFunctions
from qa.environment_variables import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH

YOUTUBE_GET_STARTED = (By.XPATH, '//ul/li/a[@data-g-name="YouTube"]')
YOUTUBE_LEARN_MORE = (By.CSS_SELECTOR, 'a[href*="youtube.com/yt/about/"]')


@when('I click Youtube\'s Get Started button')
def click_youtube_get_started(context):
    get_started_button = context.driver.find_element(*YOUTUBE_GET_STARTED)
    get_started_button.click()


@when('I click YouTube\'s Learn more')
def click_youtube_get_started(context):
    learn_more_button = context.driver.find_element(*YOUTUBE_LEARN_MORE)
    learn_more_button.click()
