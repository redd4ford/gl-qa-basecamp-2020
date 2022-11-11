from selenium.webdriver.common.by import By

from ui.config import Config
from ui.pages.base_page import BasePage


class GoogleResultsPage(BasePage):
    ALL_SEARCH_RESULTS = (By.XPATH, '//div[@class="v7W49e"]')

    def __init__(self, browser, by_keyword: str = None):
        super().__init__(browser)
        self.by_keyword = by_keyword
        if by_keyword:
            self.by_keyword = self.by_keyword.replace(' ', '+')
            self.browser.get(f'{Config.GOOGLE_BASE_URL}/search?q={by_keyword}')
            self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)

    def link(self, link_locator: tuple):
        return self.browser.find_element(*link_locator)

    def open_result_that_contains_in_link(self, partial_link: str):
        self.wait_for_presence_of_all_elements_located(GoogleResultsPage.ALL_SEARCH_RESULTS)
        self.link(link_locator=(By.PARTIAL_LINK_TEXT, partial_link)).click()
