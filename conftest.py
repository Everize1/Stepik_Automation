import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


# add cmd parameter for pytest run (chrome is default):
# pytest --browser_name=chrome
# pytest --browser_name=firefox
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store',
                     default="ru", help="ru or en")


# by default launch for each function call
@pytest.fixture(scope="function")
def browser(request):
    # request - get browser_name from cmd
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print("\nStart Сhrome browser for test..")
        opts = Options()
        opts.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager(path=".\\driver").install()), options=opts)

    elif browser_name == "firefox":
        print("\nStart Firefox browser for test..")
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager(path=".\\driver").install()))

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(10)
    yield browser
    print("\nQuit browser..")
    browser.quit()
