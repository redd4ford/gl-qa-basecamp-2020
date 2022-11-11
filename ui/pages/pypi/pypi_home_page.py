from selenium.webdriver.common.by import By

from ui.config import Config
from ui.pages.base_page import BasePage
from ui.pages.pypi import PyPIResultsPage


class PyPIHomePage(BasePage):
    URL = Config.PYPI_BASE_URL

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

    def search_project(self, phrase: str, enter: bool = False) -> PyPIResultsPage:
        self.search_field.send_keys(phrase)
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)

        self.click_button_or_press_enter_on_input(
            input=self.search_field,
            button=self.search_button,
            enter=enter,
        )

        return PyPIResultsPage(self.browser)
