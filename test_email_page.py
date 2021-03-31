from pages.email_page import MailPage
from pages.login_page import LoginPage
import test_constants


class TestEmailPage:

    def test_send_email(self, browser):
        page = LoginPage(browser, test_constants.login_page)
        page.open_url()
        page.login(test_constants.test_login, test_constants.test_password)
        inbox = MailPage(browser, test_constants.inbox_page)
        inbox.click_write_email_button()
        inbox.specify_to_field()
        inbox.go_to_email_body_and_specify_body()
        inbox.click_send_button()
        inbox.success_popup_appears()


