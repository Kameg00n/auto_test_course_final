import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()