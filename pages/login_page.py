from pages.base_page import BasePageElement
from locators import LoginPageLocators
import test_constants
import time


class LoginPage(BasePageElement):

    def input_login(self, login):
        login_field = self.find_present_element_by_xpath(LoginPageLocators.INPUT_LOGIN_FIELD)
        self.input_data(login_field, login)

    def press_input_password_button(self):
        self.press_button(LoginPageLocators.INPUT_PASSWORD_BUTTON)

    def input_password(self, password):
        password_field = self.find_present_element_by_xpath(LoginPageLocators.INPUT_PASSWORD_FIELD)
        self.input_data(password_field, password)

    def press_login_button(self):
        login_button = self.find_present_element_by_xpath(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def login(self, login, password):
        self.input_login(login)
        self.press_input_password_button()
        self.input_password(password)
        self.press_login_button()

    def user_is_redirected_to_inbox_page(self):
        #TODO: fix assertion
        time.sleep(3)
        assert self.get_current_url().startswith(test_constants.inbox_page)






