from pages.base_page import BasePage
from pages.locators import PromoPageLocators, MainPageLocators


class PromoPage(BasePage):
    def add_to_basket_promo_full_tests(self):
        # self.should_be_url() #Вызываем метод для проверки корректности URL
        add_basket = self.browser.find_element(*PromoPageLocators.ADD_TO_BASKET)
        add_basket.click()  # Действие, клик по кнопке "добавить в корзину"
        self.solve_quiz_and_get_code()  # Вызов математической операции из класса BasePage(по заданию дано)
        self.should_be_correct_notification()  # Вызов метода для проверки текста уведомления о добавлении в корзину
        self.should_be_price_notification()  # Вызов метода для проверки текста "стоимость корзины теперь..."
        self.should_be_correct_notification_for_price()  # Вызов метода для проверки самой стоимости цены

    # def should_be_url(self):
    # assert '?promo=newYear' in self.browser.current_url, 'newYear missing from url'

    def should_be_correct_notification(self):
        assert 'был добавлен в вашу корзину.' in self.browser.find_element(
            *PromoPageLocators.NOTIFICATION_OF_ADD).text, \
            f'Notification of adding to the cart is incorrect, actual result {self.browser.find_element(*PromoPageLocators.NOTIFICATION_OF_ADD).text}'
        # Проверка на корректность текста нотификации о добавлении в корзину
        message = self.browser.find_element(*PromoPageLocators.NOTIFICATION_OF_ADD_NAME_BOOK).text
        # Дергаем и переводим в текст нужное имя книги в сообщении о добавлении в корзину
        product_name = self.browser.find_element(*PromoPageLocators.NAME_BOOK).text
        # Дергаем и переведим в текст нужное имя книги на странице товара
        assert message == product_name, 'Name in message != name in pages'

    def should_be_price_notification(self):
        assert 'Стоимость корзины теперь составляет' in self.browser.find_element(
            *PromoPageLocators.NOTIFICATION_PRICE).text, \
            f'Notification indicating the cost is incorrect, actual result {self.browser.find_element(*PromoPageLocators.NOTIFICATION_PRICE).text}'
        # Проверка, что текст нотификации корректен

    def should_be_correct_notification_for_price(self):
        assert self.browser.find_element(*PromoPageLocators.PRICE_BOOK).text in self.browser.find_element(
            *PromoPageLocators.NOTIFICATION_PRICE_IN_BASKET).text, \
            f'The price in the notification is incorrect, actual result {self.browser.find_element(*PromoPageLocators.NOTIFICATION_PRICE_IN_BASKET).text}'
        # Проверка, что стоимость товара равна стоимости в нотификации

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PromoPageLocators.NOTIFICATION_OF_ADD), \
            "Success message is presented, but should not be" #Проверка, что сообщение о добавлении в корзину отсутствует при входе на страницу

    def should_be_disappear_message(self):
        add_basket = self.browser.find_element(*PromoPageLocators.ADD_TO_BASKET)
        add_basket.click()
        assert self.is_disappeared(*PromoPageLocators.NOTIFICATION_OF_ADD), \
           "The message has not disappeared"

    def should_not_be_success_message_after_add(self):
        add_basket = self.browser.find_element(*PromoPageLocators.ADD_TO_BASKET)
        add_basket.click()
        self.should_not_be_success_message()


