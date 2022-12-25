from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_LOGIN = (By.ID, 'com.ajaxsystems:id/login')
    BUTTON_CREATE_ACCOUNT = (By.ID, 'com.ajaxsystems:id/registration')
    BUTTON_FORGOT_PASSWORD = (By.ID, 'com.ajaxsystems:id/forgot')
    BUTTON_NEXT = (By.ID, 'com.ajaxsystems:id/next')
    INPUT_EMAIL = (By.ID, 'com.ajaxsystems:id/login')
    INPUT_PASSWORD = (By.ID, 'com.ajaxsystems:id/password')


class SidebarLocators:
    BUTTON_SIDEBAR = (By.ID, 'com.ajaxsystems:id/menuDrawer')
    SIDEBAR = (By.ID, 'com.ajaxsystems:id/nav_view')
    SIDEBAR_BUTTON_ADD_HUB = (By.ID, 'com.ajaxsystems:id/addHub')
    SIDEBAR_BUTTON_SETTINGS = (By.ID, 'com.ajaxsystems:id/settings')
    SIDEBAR_BUTTON_HELP = (By.ID, 'com.ajaxsystems:id/help')
    SIDEBAR_BUTTON_LOGS = (By.ID, 'com.ajaxsystems:id/logs')
    SIDEBAR_BUTTON_DOCUMENTATION = (By.ID, 'com.ajaxsystems:id/documentation_text')


class PagesLocators:
    PAGE_ADD_HUB = (By.ID, 'com.ajaxsystems:id/toolbarTitle')
    PAGE_SETTINGS = (By.ID, 'com.ajaxsystems:id/toolbarTitle')
    PAGE_HELP = (By.ID, 'com.ajaxsystems:id/toolbarTitle')
    PAGE_LOGS = (By.ID, 'com.ajaxsystems:id/title')
    PAGE_DOCUMENTATION = (By.ID, 'com.ajaxsystems:id/toolbarTitle')
