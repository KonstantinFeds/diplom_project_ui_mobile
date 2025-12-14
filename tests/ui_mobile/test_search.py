
from tests.pages_ui_mobile.search_page import SearchPage


search_page = SearchPage()

def test_search_by_text(skip_onboarding):
    (search_page.open_search_click()
     .insert_text('Gladiator 2000 film')
     .assert_name_result('Gladiator (2000 film)'))


