from .login_page import LoginPage
from framework.locators import SidebarLocators


class SideBar(LoginPage):
    def open_sidebar(self):
        self.click_element(SidebarLocators.BUTTON_SIDEBAR)

    def page_title(self, locator: tuple) -> bool:
        element = self.find_element(locator)
        return element.text
