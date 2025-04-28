import time
from typing import Tuple
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
  def __init__(self, driver):
    self.driver = driver

  def click(self, by_locator: Tuple[str, str], timeout: int = 10):
    return (
      WebDriverWait(self.driver, timeout)
      .until(expected_conditions.visibility_of_element_located(by_locator))
      .click()
    )

  def get_element(self, by_locator: Tuple[str, str], timeout: int = 10):
    return WebDriverWait(self.driver, timeout).until(
      expected_conditions.visibility_of_element_located(by_locator)
    )

  def send_keys(self, by_locator: Tuple[str, str], text: str):
    WebDriverWait(self.driver, 10).until(
      expected_conditions.visibility_of_element_located(by_locator)
    ).send_keys(text)

  def is_element_exist(self, by_locator: Tuple[str, str], timeout: int = 10):
    try:
      WebDriverWait(self.driver, timeout).until(
        expected_conditions.visibility_of_element_located(by_locator)
      )
      return True
    except:
      return False
  
  def scroll_to_element(self, name):
    if self.driver.capabilities['platformName'] == "Android":
      self.scroll_into_view_android(name=name, max_scrolls=5, steps=200)
    else:
      # self.driver.execute_script("mobile: scroll", {"direction": "down", "predicateString": f'name == "{name}"'})
      self.scroll_into_view_ios(locator=(AppiumBy.XPATH, f'//XCUIElementTypeOther[@name="{name}"]/following-sibling::XCUIElementTypeSwitch'))
  
  def scroll_into_view_android(self, name, max_scrolls=10, steps=55):
    scrollable = 'new UiScrollable(new UiSelector().scrollable(true))'
    for _ in range(max_scrolls):
      try:
        element = self.driver.find_element(
          AppiumBy.ANDROID_UIAUTOMATOR,
          f'new UiSelector().description("{name}")'
        )
        return element
      except NoSuchElementException:
        try:
          self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'{scrollable}.scrollForward({steps})'
          )
          time.sleep(1)
        except Exception as e:
          print("더 이상 스크롤 불가", e)
          break
    raise Exception(f"{max_scrolls}회 스크롤 동안 description이 '{name}'인 element를 찾지 못함.")
  
  def swipe_up(self, velocity=1000, percent=0.7):
    self.driver.execute_script("mobile: swipe", {
      "direction": "up",
      "velocity": velocity,
      "percent": percent
    })

  def scroll_into_view_ios(self, locator):
    for _ in range(5):
      try:
        return self.get_element(locator, timeout=2)
      except TimeoutException:
        self.swipe_up(velocity=300, percent=0.5)
    raise Exception(f"스크롤 후에 {locator} element를 찾지 못함.")
