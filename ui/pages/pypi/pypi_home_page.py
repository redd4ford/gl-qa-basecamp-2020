from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ui.config.config import Config
from ui.pages.base_page import BasePage
from ui.pages.pypi.pypi_results_page import PyPIResultsPage


class PyPIHomePage(BasePage):
    URL = Config.PYPI_URL

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.CLASS_NAME, 'search-form__button')

    def __init__(self, browser):
        super().__init__(browser)
        self.open()

    def open(self):
        self.browser.get(PyPIHomePage.URL)
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)
        for locator in [PyPIHomePage.SEARCH_FIELD, PyPIHomePage.SEARCH_BUTTON]:
            self.wait_for_presence_of_all_elements_located(locator)

    @property
    def search_field(self):
        return self.browser.find_element(*PyPIHomePage.SEARCH_FIELD)

    @property
    def search_button(self):
        return self.browser.find_element(*PyPIHomePage.SEARCH_BUTTON)

    def search_project(self, phrase, enter=False):
        self.search_field.send_keys(phrase)
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)
        if enter:
            self.search_field.send_keys(Keys.RETURN)
        else:
            self.search_button.click()

        return PyPIResultsPage(self.browser)
