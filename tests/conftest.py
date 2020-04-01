import pytest

from sample_app import create_app
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    ctx = app.app_context()
    ctx.push()

    yield app.test_client()

    ctx.pop()


@pytest.yield_fixture
def web_client():
    options = Options()
    options.headless = True
    firefox = webdriver.Firefox(options=options)
    firefox.implicitly_wait(3)

    yield firefox

    firefox.close()
    firefox.quit()
