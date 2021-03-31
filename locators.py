
class LoginPageLocators:

    INPUT_LOGIN_FIELD = '//input[@data-testid="login-input"]'
    INPUT_PASSWORD_BUTTON = '//button[@data-testid="enter-password"]'
    INPUT_PASSWORD_FIELD = '//input[@data-testid="password-input"]'
    LOGIN_BUTTON = '//button[@data-testid="login-to-mail"]'

class MailPageLocators:

    WRITE_EMAIL_BUTTON = '//a[@href="/compose/"]'
    SEND_EMAIL_POPUP = '//*[contains(@class,"compose-app_window")]'
    TO_FIELD = SEND_EMAIL_POPUP + '//div[@data-type="to"]//input'
    SEND_BUTTON = SEND_EMAIL_POPUP + '//div[@class="compose-app__footer"]//span[@data-title-shortcut="Ctrl+Enter"]'
    EMAIL_HAS_BEEN_SENT_POPUP = '//div[@class="layer-sent-page"][1]'
