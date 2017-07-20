import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class FindTest():

    def test(self):

        self.browser = Browser()
        self.driver = self.browser.get_browser_driver()
        self.driver.get('https://letskodeit.teachable.com/p/practice')
        print(self.driver.title)
        time.sleep(20)
        self.driver.captured_logs = ['']
        for entry in self.driver.get_log('browser'):
            self.driver.captured_logs.append(entry)
            print (entry)

        # self.elem = self.driver.find_element(
        #     By.LINK_TEXT, 'Login')  # Find the search box
        # elem.send_keys('seleniumhq' + Keys.RETURN)

        self.elem = self.driver.find_element(
            By.XPATH, '//*[@id="navbar"]//ul/li'
        )
        self.elem.click()
        time.sleep(5)
        # print (len(self.elem))
        self.driver.quit()

ff = FindTest()
ff.test()
