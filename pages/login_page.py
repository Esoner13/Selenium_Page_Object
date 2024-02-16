from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.url, "login is absent in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators. REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.EMAIL)
        mail.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        pass2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()

