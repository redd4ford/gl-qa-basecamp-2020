from urllib.parse import urljoin

from ui.config import Config
from ui.config import PyPIEndpoints
from ui.pages.pypi import PyPIHomePage


def test_project_can_be_found_and_opened():
    pypi_home_page = PyPIHomePage(Config.DRIVER)
    pypi_results_page = pypi_home_page.search_project('selenium')
    pypi_results_page.browser.implicitly_wait(1)
    pypi_results_page.open_project_by_number(0)
    assert (
        urljoin(Config.PYPI_BASE_URL, PyPIEndpoints.PY_PI_PROJECT_URL) in Config.DRIVER.current_url
    )
