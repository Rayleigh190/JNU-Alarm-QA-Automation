from appium import webdriver
import os
from appium.options.android import UiAutomator2Options

def before_all(context):
    # platform = os.getenv("PLATFORM", "Android")  # "iOS" or "Android"
    platform = "iOS"  # "iOS" or "Android"

    if platform == "iOS":
        desired_caps = {
            "platformName": "iOS",
            "platformVersion": "16.4",
            "deviceName": "iPhone 8",
            "automationName": "XCUITest",
            "bundleId" : "com.rayleigh.JNU-Alarm",
            "autoAcceptAlerts": True,
            "noReset": True,
            "fullReset": False
        }
    else:
        desired_caps = {
            "platformName": "Android",
            "appPackage": "com.jnu_alarm.android",
            "automationName": "UiAutomator2",
            "autoGrantPermissions": True,
            "autoAcceptAlerts": True,
            "noReset": True,
            "fullReset": False
        }
    
    context.driver = webdriver.Remote("http://localhost:4723", options=UiAutomator2Options().load_capabilities(desired_caps))
    context.driver.implicitly_wait(10) 

def after_all(context):
    context.driver.quit()
