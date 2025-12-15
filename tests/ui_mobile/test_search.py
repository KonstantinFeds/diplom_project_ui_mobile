from tests.pages_ui_mobile.onboarding_page import OnboardingPage
from tests.pages_ui_mobile.search_page import SearchPage

onboarding_page = OnboardingPage()
search_page = SearchPage()

def test_search_by_text():
    onboarding_page.skip_onboarding_button_click()
    (search_page.open_search_click()
     .insert_text('Gladiator 2000 film')
     .assert_name_result('Gladiator (2000 film)'))


