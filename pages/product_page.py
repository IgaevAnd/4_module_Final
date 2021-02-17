import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        # находим и нажимаем на кнопку добавить в корзину
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket.click()
        # проходим промт и алерт
        # self.solve_quiz_and_get_code()

    def should_be_massage_product_added_to_basket(self):
        # сохраням переменные имени продукта и имени продукта в сообщения об успешном добавлении продуктав корзину
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message_add = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_SUCCESS_ADDED_TO_BASKET).text
        # проверяем наличие сообщения об успешном добавлении товара в корзину
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET), f"There is no message " \
                                                                                              f"about successful " \
                                                                                              f"addition {product_name}to basket "
        # проверяем равенство имени продукта и имени продукта в сообщении об успешном доавлении в корзину
        assert product_name == product_name_in_message_add, f"{product_name} != {product_name_in_message_add}"

    def should_be_message_price_basket(self):
        # сохраням переменные имени продукта, цены продукта и общей стоимости корзины
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_message_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE_PRICE_BASKET).text
        # проверяем наличие сообщения о цене корзины
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE_BASKET), f"There is no message about the " \
                                                                                   f"price of the {product_name.text} in the basket"
        # проверяем оавенство цены продукта и общей стоимости корзины
        assert product_price == product_price_in_message_price, f"{product_name} != {product_price_in_message_price}"

    def should_not_be_success_message(self):
        # is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET), "Success message is " \
                                                                                                  "presented, " \
                                                                                                  "but should not be "

    def should_not_be_success_message_disappeared(self):
        # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET), "Success message is " \
                                                                                          "presented, " \
                                                                                          "but should not be "
