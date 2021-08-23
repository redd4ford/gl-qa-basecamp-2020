from ui.config.config import Config
from ui.pages.gl.gl_careers_page import GLCareersPage


def test_careers_page_search_field_exists():
    careers_page = GLCareersPage(Config.DRIVER)
    careers_page.open()
    assert careers_page.check_field_exists(), 'Search field is missing'


def test_careers_page_can_search():
    careers_page = GLCareersPage(Config.DRIVER)
    results_page = careers_page.search_vacancy('QA')
    vacancy_page = results_page.open_vacancy_by_number(0)
    print(vacancy_page.vacancy_title)
    assert 'qa' in vacancy_page.vacancy_title
