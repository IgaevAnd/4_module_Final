from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, f"Cant find word {LoginPageLocators.LOGIN_URL} in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        new_login_email = self.browser.find_element(*LoginPageLocators.ID_NEW_LOGIN_EMAIL)
        new_login_email.send_keys(email)
        new_login_password1 = self.browser.find_element(*LoginPageLocators.ID_NEW_LOGIN_PASSWORD1)
        new_login_password1.send_keys(password)
        new_login_password2 = self.browser.find_element(*LoginPageLocators.ID_NEW_LOGIN_PASSWORD2)
        new_login_password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

