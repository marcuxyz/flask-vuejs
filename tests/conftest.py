import pytest

from sample_app import create_app
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options
