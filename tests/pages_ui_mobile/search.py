from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from tests.pages_ui_mobile.locators_ui_mobile import LocatorsMob


class SearchPage:

    def skip_onboarding_click(self):
        browser.element((AppiumBy.ID, LocatorsMob.CKIP_ONBOARDING_BUTTON)).click()

        return self

    def open_search_click(self):
        browser.element((AppiumBy.ID, LocatorsMob.OPEN_SEARCH_BUTTON)).click()

        return self


    def insert_text(self,value):
        browser.element((AppiumBy.ID, LocatorsMob.SEARCH_TEXT_INPUT)).type(value)

        return self


    def assert_name_result(self,value):
        browser.element((AppiumBy.ID, LocatorsMob.RESULT_LIST)).should(have.exact_text(value))