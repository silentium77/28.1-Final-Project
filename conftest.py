import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome('C:/Users/zimin/PycharmProjects/FinalProject/chromedriver.exe')
    driver.implicitly_wait(10)

    yield driver
    driver.quit()