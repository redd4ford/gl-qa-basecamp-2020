from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from ui.config.config import Config


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_presence_of_all_elements_located(self, locator, timeout=Config.DEFAULT_TIMEOUT):
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator)
        )

    def click_element_from_list_of_elements(self, locator, number_of_element, timeout=Config.DEFAULT_TIMEOUT):
        elements = WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator)
        )
        elements[number_of_element].click()
