import time
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from qa.analytics.features.steps.common import CommonFunctions
from qa.settings import BASE_URL, DRIVER, SELENIUM, SL_DC, QA_FOLDER_PATH


FOOTER_CAREER_LINK = (By.XPATH, '//li[@id="footer-sitemap-about"]//lI/a[@data-g-label="Careers"]')

@when('I click the Careers link in the footer')
def click_youtube_get_started(context):
    wait = WebDriverWait(context.driver, 5, 0.25)
    context.footer_careers = wait.until(EC.element_to_be_clickable((FOOTER_CAREER_LINK)))
    context.footer_careers.click()
