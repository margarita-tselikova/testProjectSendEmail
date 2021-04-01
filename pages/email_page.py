from pages.base_page import BasePageElement
from locators import MailPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import test_constants

class MailPage(BasePageElement):

    def click_write_email_button(self):
        write_email_button = self.find_clickable_element_by_xpath(MailPageLocators.WRITE_EMAIL_BUTTON)
        write_email_button.click()

    def specify_to_field(self):
        to_field = self.find_present_element_by_xpath(MailPageLocators.TO_FIELD)
        self.input_data(to_field, test_constants.test_email)

    def go_to_email_body_and_specify_body(self):
        to_field = self.find_present_element_by_xpath(MailPageLocators.TO_FIELD)
        to_field.click()
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.TAB * 3)
        actions.send_keys('test ' + str(datetime.now()))
        actions.perform()

    def click_send_button(self):
        send_button = self.find_clickable_element_by_xpath(MailPageLocators.SEND_BUTTON)
        send_button.click()


    def success_popup_appears(self):
        assert self.check_exists_by_xpath(MailPageLocators.EMAIL_HAS_BEEN_SENT_POPUP)
