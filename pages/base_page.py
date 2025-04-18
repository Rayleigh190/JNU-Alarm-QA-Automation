from typing import Tuple

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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