from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SettingPage(BasePage):
  notice_nav_title = (AppiumBy.ACCESSIBILITY_ID, 'notice_nav_title')
  tabbar_setting_button = (AppiumBy.ACCESSIBILITY_ID, 'tabbar_setting_button')
  academic_setting_menu = (AppiumBy.ACCESSIBILITY_ID, '학사/장학 알림')
  acdemic_switch = (AppiumBy.XPATH, '//android.view.View[@content-desc="학사 알림"]/android.widget.Switch')

  def click_setting_button(self):
    self.click(self.tabbar_setting_button)

  def click_academic_setting_menu(self):
    self.click(self.academic_setting_menu)

  def toggle_academic_switch(self):
    self.click(self.acdemic_switch)

  def is_academic_switch_on(self):
    return self.get_element(self.acdemic_switch).get_attribute('checked') == 'true'

  def is_academic_switch_off(self):
    return self.get_element(self.acdemic_switch).get_attribute('checked') == 'false'
