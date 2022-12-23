from .page import Page
from .locators import LoginPageLocators, MainPageLocators


class LoginPage(Page):
    def login_user(self, email: str, password: str):
        self.click_element(LoginPageLocators.BUTTON_LOGIN)
        self.write_to_input(LoginPageLocators.INPUT_EMAIL, email)
        self.write_to_input(LoginPageLocators.INPUT_PASSWORD, password)
        self.click_element(LoginPageLocators.BUTTON_NEXT)

    def user_on_main_page(self) -> bool:
        return self.check_element_exist(MainPageLocators.BUTTON_SIDE_BAR)


