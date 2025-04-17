from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NoticePage:
    def __init__(self, driver):
        self.driver = driver

    def tap_setting(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'tabbar_setting_button'))
        ).click()

    def is_notice_screen_displayed(self):
        try:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'notice_nav_title')
            return True
        except:
            return False
