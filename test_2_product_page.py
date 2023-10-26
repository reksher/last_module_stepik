import pytest
from pages.product_page import PromoPage


link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'


@pytest.mark.xfail(reason="need for quest")
def test_guest_cant_see_success_message(browser):
    page = PromoPage(browser, link)
    page.open()
    page.should_not_be_success_message_after_add()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = PromoPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="need for quest")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = PromoPage(browser, link)
    page.open()
    page.should_be_disappear_message()

