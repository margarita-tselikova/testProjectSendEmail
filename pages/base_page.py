from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageElement:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_url(self):
        self.browser.get(self.url)

    def find_present_element_by_xpath(self, xpath):
        element = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element

    def find_clickable_element_by_xpath(self, xpath):
        element = WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return element

    def check_exists_by_xpath(self, xpath):
        try:
            WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except NoSuchElementException:
            return False
        return True

    def input_data(self, element, data):
        element.clear()
        element.send_keys(data)

    def press_button(self, xpath):
        button = self.find_clickable_element_by_xpath(xpath)
        button.click()

    def get_current_url(self):
        return self.browser.current_url
