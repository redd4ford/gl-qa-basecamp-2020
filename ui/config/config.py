import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Config:
    # OLD WAY
    # WEBDRIVER_PATH = os.getenv('GECKO_PATH', '/home/yehorova_v/personal/geckodriver')
    # DRIVER = webdriver.Firefox(executable_path=WEBDRIVER_PATH)
    # NEW WAY
    DRIVER = webdriver.Chrome(ChromeDriverManager().install())
    DEFAULT_TIMEOUT: int = 10
    GLOBAL_LOGIC_BASE_URL: str = os.getenv('GL_URL', 'https://www.globallogic.com/ua')
    GOOGLE_BASE_URL: str = os.getenv('GO_URL', 'https://www.google.com')
    PYPI_BASE_URL: str = os.getenv('PYPI_URL', 'https://pypi.org')
