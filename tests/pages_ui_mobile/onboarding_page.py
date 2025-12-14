from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from tests.pages_ui_mobile.locators import LocatorsMob


class OnboardingPage:

    def skip_onboarding_button_click(self):
        browser.element((AppiumBy.ID, LocatorsMob.CKIP_ONBOARDING_BUTTON)).click()

        return self

    def add_or_edit_languages_button_click(self):
        browser.element((AppiumBy.ID, LocatorsMob.ADD_OR_EDIT_LANGUAGES_BUTTON)).click()

        return self

    def add_language_button_click(self):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, LocatorsMob.ADD_LANGUAGE_BUTTON)).click()

        return self


    def open_search_tap(self):
        (browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, LocatorsMob.ADD_LANGUAGE_OPEN_SEARCH))
         .click())

        return self

    def search_input_active(self):
        (browser.element((AppiumBy.ANDROID_UIAUTOMATOR, LocatorsMob.ADD_LANGUAGE_SEARCH_INPUT))
         .click())

        return self

    def insert_language_in_search(self,value):
        browser.element((AppiumBy.CLASS_NAME, LocatorsMob.INSERT_LANGUAGE)).type(value)

        return self

    def result_click(self):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, LocatorsMob.LANGUAGE_RESULT)).click()

        return self

    def back_button_click(self):
        browser.element((AppiumBy.ACCESSIBILITY_ID, LocatorsMob.BACK_BUTTON)).click()

        return self

    def assert_available_language(self,value):
        browser.all((AppiumBy.ID, LocatorsMob.AVAILABLE_LANGUAGE))[1].should(
            have.text(value))

        return self