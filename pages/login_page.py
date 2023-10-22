from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"Link is incorrect, actual result {self.browser.current_url}"

    def should_be_login_form(self,):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.button_log), 'Button for login is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.button_reg), 'Button for registration is not presented'



