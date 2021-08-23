from ui.config.config import Config
from ui.pages.pypi.pypi_home_page import PyPIHomePage


def test_careers_page_search_field_exists():
    pypi_home_page = PyPIHomePage(Config.DRIVER)
    pypi_results_page = pypi_home_page.search_project('selenium')
    pypi_results_page.browser.implicitly_wait(1)
    pypi_results_page.open_project_by_number(0)
    assert 'https://pypi.org/project/' in Config.DRIVER.current_url
