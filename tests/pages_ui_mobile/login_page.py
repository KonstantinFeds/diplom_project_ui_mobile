from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.pages_ui_mobile.locators import LocatorsMob


class LoginPage:

    def more_menu_click(self):
        browser.element((AppiumBy.ACCESSIBILITY_ID, LocatorsMob.MORE_MENU_BUTTON)).click()
        return self

    def go_to_create_account_page(self):
        browser.element((AppiumBy.ID,LocatorsMob.LOGIN_MENU_BUTTON)).click()
        return self

    def go_to_login_page(self):
        browser.element((AppiumBy.ID,LocatorsMob.LOGIN_PAGE_BUTTON)).click()
        return self

    def username_tap(self):
        browser.element((AppiumBy.XPATH,LocatorsMob.USERNAME)).click()
        return self

    def insert_username(self,value):
        browser.element((AppiumBy.XPATH, LocatorsMob.USERNAME)).type(value)
        return self

    def password_tap(self):
        browser.element((AppiumBy.XPATH,LocatorsMob.PASSWORD)).click()
        return self


    def insert_password(self,value):
        browser.element((AppiumBy.XPATH,LocatorsMob.PASSWORD)).type(value)

        return self


    def login_button_click(self):
        browser.element((AppiumBy.ID,LocatorsMob.LOGIN_BUTTON)).click()

        return self

    def assert_error_msg_login(self,value):
        browser.element((AppiumBy.ID,LocatorsMob.ERROR_MSG_LOGIN)).should(have.exact_text(value))

        return self