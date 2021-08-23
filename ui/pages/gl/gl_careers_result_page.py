from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from ui.config.config import Config
from ui.config.endpoints import Endpoints
from ui.pages.base_page import BasePage
from ui.pages.gl.gl_careers_vacancy_page import GLCareersVacancyPage


class GLCareersResultPage(BasePage):
    URL = urljoin(Config.GLOBAL_LOGIC_BASE_URL, Endpoints.GLOBAL_LOGIC_CAREERS_SEARCH_URL)

    GL_SEARCH_RESULTS = (By.XPATH, '//div[@class="career-pagelink"]//p[1]')

    def __init__(self, browser, by_keyword=None):
        super().__init__(browser)
        self.open(by_keyword)

    def open(self, by_keyword=None):
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT)
        self.browser.get(
            f'{GLCareersResultPage.URL}/?keywords={by_keyword}&experience=&locations=&c='
        )

    def open_vacancy_by_number(self, number):
        self.wait_for_presence_of_all_elements_located(self.GL_SEARCH_RESULTS)
        self.click_element_from_list_of_elements(
            self.GL_SEARCH_RESULTS, number)
        return GLCareersVacancyPage(self.browser)
