from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self):
        assert self.is_element_present(
            *LoginPageLocators.EMAIL_FIELD), "Did not found email field"
        assert self.is_element_present(
            *LoginPageLocators.PASS1_FIELD), "Did not found pass1 field"
        assert self.is_element_present(
            *LoginPageLocators.PASS2_FIELD), "Did not found pass2 field"

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        email_field_elem = self.browser.find_element(
            *LoginPageLocators.EMAIL_FIELD)
        pass1_field_elem = self.browser.find_element(
            *LoginPageLocators.PASS1_FIELD)
        pass2_field_elem = self.browser.find_element(
            *LoginPageLocators.PASS2_FIELD)

        email_field_elem.send_keys(email)
        pass1_field_elem.send_keys(password)
        pass2_field_elem.send_keys(password)

        self.click(*LoginPageLocators.REGISTRATION_SUBMIT)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Not a login page!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Did not found login field"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Did not found register form"

    def register_new_user(self):
        assert self.is_element_present(
            *LoginPageLocators.EMAIL_FIELD), "Did not found email field"
        assert self.is_element_present(
            *LoginPageLocators.PASS1_FIELD), "Did not found pass1 field"
        assert self.is_element_present(
            *LoginPageLocators.PASS2_FIELD), "Did not found pass2 field"

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        email_field_elem = self.browser.find_element(
            *LoginPageLocators.EMAIL_FIELD)
        pass1_field_elem = self.browser.find_element(
            *LoginPageLocators.PASS1_FIELD)
        pass2_field_elem = self.browser.find_element(
            *LoginPageLocators.PASS2_FIELD)

        email_field_elem.send_keys(email)
        pass1_field_elem.send_keys(password)
        pass2_field_elem.send_keys(password)

        self.click(*LoginPageLocators.REGISTRATION_SUBMIT)
