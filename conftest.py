import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from pages.setting_page import SettingPage

def pytest_addoption(parser):
  parser.addoption(
    "--platform", 
    action="store", 
    default="android", 
    help="테스트를 실행할 플랫폼 : android or ios"
  )


@pytest.fixture(scope="session")
def platform(request):
  return request.config.getoption("--platform")


@pytest.fixture(scope="module")
def driver(platform):
  if platform == "ios":
    url = "http://localhost:4725"
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
    url = "http://localhost:4723"
    desired_caps = {
      "platformName": "Android",
      "appPackage": "com.jnu_alarm.android",
      "automationName": "UiAutomator2",
      "autoGrantPermissions": True,
      "autoAcceptAlerts": True,
      "noReset": True,
      # "fullReset": False
    }

  driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(desired_caps))
  # driver.implicitly_wait(10) 
  yield driver
  if platform == "android":
    driver.terminate_app("com.jnu_alarm.android")
  else:
    driver.terminate_app("com.rayleigh.JNU-Alarm")
  driver.quit()


@pytest.fixture(scope="module")
def setting_page(driver, request):
  page = SettingPage(driver)
  page.go_to_settings(request.param)
  return page