from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SettingPage(BasePage):
  tabbar_setting_button = (AppiumBy.ACCESSIBILITY_ID, 'tabbar_setting_button')

  def go_to_settings(self, accessibility_id):
    self.click(self.tabbar_setting_button)
    self.click((AppiumBy.ACCESSIBILITY_ID, accessibility_id))

  def get_switch(self, name):
    if self.driver.capabilities['platformName'] == "Android":
      return self.get_element((AppiumBy.XPATH, f'//android.view.View[@content-desc="{name}"]/android.widget.Switch'))
    else:
      return self.get_element((AppiumBy.XPATH, f'//XCUIElementTypeOther[@name="{name}"]/following-sibling::XCUIElementTypeSwitch'))

  def toggle_switch(self, name):
    self.get_switch(name).click()

  def is_switch_on(self, name):
    if self.driver.capabilities['platformName'] == "Android":
      return self.get_switch(name).get_attribute('checked') == 'true'
    else:
      return self.get_switch(name).get_attribute('value') == '1'
  
  def is_switch_off(self, name):
    if self.driver.capabilities['platformName'] == "Android":
      return self.get_switch(name).get_attribute('checked') == 'false'
    else:
      return self.get_switch(name).get_attribute('value') == '0'
  