import pytest

from framework.locators import SidebarLocators, PagesLocators


def test_sidebar_open(sidebar_fixture):
    page = sidebar_fixture
    page.click_element(SidebarLocators.BUTTON_SIDEBAR)
    assert page.check_element_exist(SidebarLocators.SIDEBAR)


@pytest.mark.parametrize(
    'locator',
    [
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_ADD_HUB,
            id='Add Hub exist in sidebar'
        ),
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_SETTINGS,
            id='App Settings exist in sidebar'
        ),
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_HELP,
            id='Help exist in sidebar'
        ),
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_LOGS,
            id='Report a problem exist in sidebar'
        ),
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_DOCUMENTATION,
            id='Terms of Service exist in sidebar'
        ),
    ]
)
def test_sidebar_content(locator: tuple, sidebar_fixture):
    page = sidebar_fixture
    if not page.check_element_exist(SidebarLocators.SIDEBAR):
        page.open_sidebar()
    assert page.check_element_exist(locator)


@pytest.mark.parametrize(
    'button,locator,title',
    [
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_ADD_HUB,
            PagesLocators.PAGE_ADD_HUB,
            'Add hub',
            id='check redirect on Add Hub page'
        ),
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_SETTINGS,
            PagesLocators.PAGE_SETTINGS,
            'Account',
            id='check redirect on App Settings page'
        ),
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_HELP,
            PagesLocators.PAGE_HELP,
            'Installation Manuals',
            id='check redirect on Help page'
        ),
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_LOGS,
            PagesLocators.PAGE_LOGS,
            'Report a problem',
            id='check redirect on Report a problem page'
        ),
        pytest.param(
            SidebarLocators.SIDEBAR_BUTTON_DOCUMENTATION,
            PagesLocators.PAGE_DOCUMENTATION,
            'Terms of Service',
            id='check redirect on Terms of Service page'
        ),
    ]
)
def test_sidebar_redirect(button: tuple, locator: tuple, title: str, sidebar_fixture):
    page = sidebar_fixture
    if not page.check_element_exist(SidebarLocators.SIDEBAR):
        page.open_sidebar()
    page.click_element(button)
    page.wait(5)
    assert page.page_title(locator) == title
    page.back()
