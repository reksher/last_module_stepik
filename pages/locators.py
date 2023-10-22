from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    email_reg = (By.CSS_SELECTOR, '[id="id_registration-email"]')
    password1_reg = (By.CSS_SELECTOR, '[id="id_registration-password1"]')
    password2_reg = (By.CSS_SELECTOR, '[id="id_registration-password2"]')
    button_reg = (By.CSS_SELECTOR, '[name="registration_submit"]')
    email_log = (By.CSS_SELECTOR, '[id="id_login-username"]')
    password_log = (By.CSS_SELECTOR, '[id="id_login-password"]')
    button_log = (By.CSS_SELECTOR, '[name="login_submit"]')

