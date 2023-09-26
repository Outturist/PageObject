from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name')
    parser.addoption('--user_language')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        user_language = request.config.getoption('user_language')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        # browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise Exception('--browser_name should be chrome or firefox')
    yield browser
    browser.quit()
