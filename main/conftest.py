import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class', autouse=True)
def browser_invocation():
    # Chrome Browser Invocation
    s = Service("C:\chromedriver.exe")
    driver = Chrome(service=s)
    driver.maximize_window()

    # Get into Automation practice url
    driver.get('https://reqres.in/')

    yield driver

    driver.quit()


@pytest.fixture()
def url():
    return 'https://reqres.in'

@pytest.fixture()
def filenamemode():
    return ('data.csv', 'a')
