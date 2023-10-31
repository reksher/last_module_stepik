from pages.base_page import BasePage
from pages.locators import BasketLocators, MainPageLocators


class BasketPage(BasePage):

    def should_be_notification_about_empty_basket(self):
        expected_basket = 'Ваша корзина пуста'
        actual_basket = self.browser.find_element(*BasketLocators.EMPTY_BASKET).text
        assert expected_basket in actual_basket, \
            f'The inscription about an empty basket is incorrect, actual {actual_basket}'

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketLocators.PRODUCT_IN_THE_BASKET), "The product is in the cart"

    def should_be_empty_basket_from_main_page(self):
        basket_mini = self.browser.find_element(*MainPageLocators.BASKET_MINI)
        basket_mini.click()
        self.should_be_empty_basket()
        self.should_be_notification_about_empty_basket()

    def should_be_opened_basket(self):
        basket_mini = self.browser.find_element(*MainPageLocators.BASKET_MINI)
        basket_mini.click()
        self.should_be_empty_basket()
        self.should_be_notification_about_empty_basket()


