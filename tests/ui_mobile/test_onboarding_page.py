from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_expect_text_page_four():
    browser.element((AppiumBy.ID,'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    browser.element((AppiumBy.ID,'org.wikipedia.alpha:id/search_container')).click()
    browser.element((AppiumBy.ID,'org.wikipedia.alpha:id/search_src_text')).type('Gladiator 2000 film')
    browser.element((AppiumBy.ID,'org.wikipedia.alpha:id/page_list_item_title')).should(have.exact_text('Gladiator (2000 film)'))

    #Gladiator 2000 film
