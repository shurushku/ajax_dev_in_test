import pytest
import time

from framework.sidebar import SideBar
from framework.login_page import LoginPage


@pytest.fixture(scope='session')
def user_login_fixture(driver):
    page = LoginPage(driver)
    page.login_user('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    time.sleep(5)


@pytest.fixture(scope='function')
def sidebar_fixture(user_login_fixture, driver):
    yield SideBar(driver)
