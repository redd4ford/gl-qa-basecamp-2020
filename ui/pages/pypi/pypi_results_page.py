from selenium.webdriver.common.by import By

from ui.config.config import Config
from ui.pages.base_page import BasePage


class PyPIResultsPage(BasePage):
    PYPI_SEARCH_RESULTS = (By.CLASS_NAME, 'package-snippet')

    def __init__(self, browser, urn: str = None):
        super().__init__(browser)
        if urn is not None:
            self.browser.get(Config.PYPI_URL + urn)
            self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)

    def open_project_by_number(self, number_of_project):
        self.click_element_from_list_of_elements(
            PyPIResultsPage.PYPI_SEARCH_RESULTS, number_of_project)
