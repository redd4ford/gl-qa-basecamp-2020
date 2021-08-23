import os
from selenium import webdriver


class Config:
    GECKO_DRIVER_PATH = os.getenv('GECKO_PATH', 'C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')
    DRIVER = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)
    DEFAULT_TIMEOUT = 10
    GLOBAL_LOGIC_BASE_URL = os.getenv('GL_URL', 'https://www.globallogic.com/ua')
    GOOGLE_BASE_URL = os.getenv('GO_URL', 'https://www.google.com')
    PYPI_URL = os.getenv('PYPI_URL', 'https://pypi.org')
