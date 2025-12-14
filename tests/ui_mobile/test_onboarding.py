from tests.pages_ui_mobile.onboarding_page import OnboardingPage

onboarding_page = OnboardingPage()

def test_add_language():

    (onboarding_page.add_or_edit_languages_button_click()
     .add_language_button_click()
     .open_search_tap().search_input_active()
     .insert_language_in_search('Russian')
     .result_click()
     .back_button_click()
     .assert_available_language('Русский'))

