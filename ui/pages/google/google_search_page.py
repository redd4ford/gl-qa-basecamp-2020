from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ui.config.config import Config
from ui.pages.base_page import BasePage
from ui.pages.google.google_results_page import GoogleResultsPage


class GoogleSearchPage(BasePage):
    URL = Config.GOOGLE_BASE_URL

    SEARCH_FIELD = (By.NAME, 'q')
    SEARCH_BUTTON = (By.XPATH, '//div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(GoogleSearchPage.URL)
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)
        for locator in [GoogleSearchPage.SEARCH_FIELD, GoogleSearchPage.SEARCH_BUTTON]:
            self.wait_for_presence_of_all_elements_located(locator)

    @property
    def search_field(self):
        return self.browser.find_element(*GoogleSearchPage.SEARCH_FIELD)

    @property
    def search_button(self):
        return self.browser.find_element(*GoogleSearchPage.SEARCH_BUTTON)

    def search_by_phrase(self, phrase, enter=False):
        self.search_field.send_keys(phrase)
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)
        if enter:
            self.search_field.send_keys(Keys.RETURN)
        else:
            self.search_field.submit()

        return GoogleResultsPage(self.browser, phrase)
