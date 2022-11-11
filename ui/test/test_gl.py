from ui.config import Config
from ui.pages.gl import GLCareersPage


def test_careers_page_search_field_exists():
    careers_page = GLCareersPage(Config.DRIVER)
    careers_page.open()
    assert careers_page.check_field_exists(), 'Search field is missing'


def test_careers_page_can_search():
    careers_page = GLCareersPage(Config.DRIVER)
    results_page = careers_page.search_vacancy('QA')
    vacancy_page = results_page.open_vacancy_by_number(1)
    assert 'QA' in vacancy_page.vacancy_title, 'Not a QA position'
