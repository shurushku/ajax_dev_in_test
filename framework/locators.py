from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_LOGIN = (By.ID, 'com.ajaxsystems:id/login')
    BUTTON_CREATE_ACCOUNT = (By.ID, 'com.ajaxsystems:id/registration')
    BUTTON_FORGOT_PASSWORD = (By.ID, 'com.ajaxsystems:id/forgot')
    BUTTON_NEXT = (By.ID, 'com.ajaxsystems:id/next')
    INPUT_EMAIL = (By.ID, 'com.ajaxsystems:id/login')
    INPUT_PASSWORD = (By.ID, 'com.ajaxsystems:id/password')


class MainPageLocators:
    BUTTON_SIDE_BAR = (By.ID, 'com.ajaxsystems:id/menuDrawer')
