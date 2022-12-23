from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.webelement import WebElement


class Page:

    def __init__(self, driver):
        self.driver = driver

    def check_element_exist(self, locator: tuple) -> bool:
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        else:
            return True

    def find_element(self, locator: tuple) -> WebElement:
        if not self.check_element_exist(locator):
            raise NoSuchElementException(f'Element {locator} does not exist')
        element = self.driver.find_element(*locator)
        return element

    def click_element(self, locator: tuple) -> None:
        element = self.find_element(locator)
        element.click()

    def write_to_input(self, locator: tuple, text: str) -> None:
        element = self.find_element(locator)
        element.send_keys(text)

    def wait(self, seconds: int):
        self.driver.implicitly_wait(seconds)
