from pages.login_page import LoginPage
import test_constants

class TestLoginPage:

    def test_login_as_existing_user(self, browser):
        url = test_constants.login_page
        page = LoginPage(browser, url)
        page.open_url()
        page.input_login(test_constants.test_login)
        page.press_input_password_button()
        page.input_password(test_constants.test_password)
        page.press_login_button()
        page.user_is_redirected_to_inbox_page()
