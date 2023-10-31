from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_MINI = (By.CSS_SELECTOR, ".btn-group a.btn-default")


class LoginPageLocators:
    email_reg = (By.CSS_SELECTOR, '[id="id_registration-email"]')
    password1_reg = (By.CSS_SELECTOR, '[id="id_registration-password1"]')
    password2_reg = (By.CSS_SELECTOR, '[id="id_registration-password2"]')
    button_reg = (By.CSS_SELECTOR, '[name="registration_submit"]')
    email_log = (By.CSS_SELECTOR, '[id="id_login-username"]')
    password_log = (By.CSS_SELECTOR, '[id="id_login-password"]')
    button_log = (By.CSS_SELECTOR, '[name="login_submit"]')


class PromoPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NOTIFICATION_OF_ADD = (By.CSS_SELECTOR, 'div.alert:first-child .alertinner')
    NOTIFICATION_OF_ADD_NAME_BOOK = (By.CSS_SELECTOR, 'div.alert:first-child strong')
    NAME_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    NOTIFICATION_PRICE = (By.CSS_SELECTOR, 'div.alert:last-child .alertinner p:first-of-type')
    NOTIFICATION_PRICE_IN_BASKET = (By.CSS_SELECTOR, 'div.alert:last-child strong')
    PRICE_BOOK = (By.CSS_SELECTOR, '.col-sm-6 .price_color')


class BasketLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p:first-of-type')
    PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, '.basket-title .row h2')

