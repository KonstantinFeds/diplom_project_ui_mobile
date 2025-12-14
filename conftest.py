import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser
import config
import utils.allure
from tests.pages_ui_mobile.onboarding_page import OnboardingPage


onboarding_page = OnboardingPage()

@pytest.fixture(scope='function')
def skip_onboarding():
    onboarding_page.skip_onboarding_button_click()


@pytest.fixture(scope='session',autouse=True)
def clear_allure_results():
    config.clear_allure_results()



def pytest_addoption(parser):
    parser.addoption(
        "--context", default="bstack", help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope="function", autouse=True)
def mobile_management(context):

    options = config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(
        options.get_capability("remote_url"), options=options
    )
    browser.config.timeout = 10.0

    yield

    # attach.add_screenshot()
    # attach.add_xml()
    session_id = browser.driver.session_id

    browser.quit()

    if context == "bstack":
        utils.allure.attach_bstack_video_android(session_id)
