import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from pages.setting_page import SettingPage

@pytest.fixture(scope="module")
def driver():
  platform = "Android"  # "iOS" or "Android"

  if platform == "iOS":
    desired_caps = {
      "platformName": "iOS",
      "platformVersion": "16.4",
      "deviceName": "iPhone 8",
      "automationName": "XCUITest",
      "bundleId" : "com.rayleigh.JNU-Alarm",
      "autoAcceptAlerts": True,
      "noReset": True,
      # "fullReset": False
    }
  else:
    desired_caps = {
      "platformName": "Android",
      "appPackage": "com.jnu_alarm.android",
      "automationName": "UiAutomator2",
      "autoGrantPermissions": True,
      "autoAcceptAlerts": True,
      "noReset": True,
      # "fullReset": False
    }

  driver = webdriver.Remote("http://localhost:4723", options=UiAutomator2Options().load_capabilities(desired_caps))
  driver.implicitly_wait(10) 
  yield driver
  if platform == "Android":
    driver.terminate_app("com.jnu_alarm.android")
  else:
    driver.terminate_app("com.rayleigh.JNU-Alarm")
  driver.quit()


@pytest.fixture(scope="module")
def setting_page(driver, request):
  page = SettingPage(driver)
  page.go_to_settings(request.param)
  return page