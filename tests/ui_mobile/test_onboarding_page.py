from tests.pages_ui_mobile.search import SearchPage

search_page = SearchPage()

def test_search_by_text():
    (search_page.skip_onboarding_click()
     .open_search_click()
     .insert_text('Gladiator 2000 film')
     .assert_name_result('Gladiator (2000 film)'))


