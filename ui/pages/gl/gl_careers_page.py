from urllib.parse import urljoin

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from ui.config.config import Config
from ui.config.endpoints import Endpoints
from ui.pages.base_page import BasePage
from ui.pages.gl.gl_careers_result_page import GLCareersResultPage


class GLCareersPage(BasePage):
    URL = urljoin(Config.GLOBAL_LOGIC_BASE_URL, Endpoints.GLOBAL_LOGIC_CAREERS_URL)

    SEARCH_FIELD = (By.ID, 'by_keyword')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="hero"]/div/div/div/div/div/div/div/form/div/button')
    COOKIE_ALLOW_ALL_BUTTON = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')

    def __init__(self, browser):
        super().__init__(browser)
        self.open()

    def open(self):
        self.browser.get(GLCareersPage.URL)
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)
        try:
            self.allow_cookie_button.click()
        except NoSuchElementException:
            pass

    @property
    def allow_cookie_button(self):
        return self.browser.find_element(*GLCareersPage.COOKIE_ALLOW_ALL_BUTTON)

    @property
    def search_field(self):
        return self.browser.find_element(*GLCareersPage.SEARCH_FIELD)

    @property
    def search_button(self):
        return self.browser.find_element(*GLCareersPage.SEARCH_BUTTON)

    def search_vacancy(self, vacancy, enter=False):
        self.wait_for_presence_of_all_elements_located(GLCareersPage.SEARCH_FIELD)
        self.search_field.send_keys(vacancy)
        self.wait_for_presence_of_all_elements_located(GLCareersPage.SEARCH_BUTTON)
        if enter:
            self.search_field.send_keys(Keys.RETURN)
        else:
            self.search_button.click()
        return GLCareersResultPage(self.browser, by_keyword=vacancy)

    def check_field_exists(self):
        return self.search_field is not None and self.search_field.tag_name == 'input'
