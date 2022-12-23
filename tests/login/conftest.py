import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    driver.launch_app()
    yield LoginPage(driver)
    driver.close_app()
