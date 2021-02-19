from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        # метод для добавления продукта в корзину
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_message_product_added_to_basket(self):
        # метод проверки сообщения об успешном добавлении продукта в корзину и проверки соответствия названия
        # продукта и названия продукта в сообщении
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message_add = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_SUCCESS_ADDED_TO_BASKET).text
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET), f"There is no message " \
                                                                                              f"about successful " \
                                                                                              f"addition {product_name}to basket "
        assert product_name == product_name_in_message_add, f"{product_name} != {product_name_in_message_add}"

    def should_be_message_price_basket(self):
        # метод проверки наличия сообщения о цене корзины и проверки соответствия цены продукта и цены корзины
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_message_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE_PRICE_BASKET).text
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE_BASKET), f"There is no message about the " \
                                                                                   f"price of the {product_name.text} in the basket"
        assert product_price == product_price_in_message_price, f"{product_name} != {product_price_in_message_price}"

    def should_not_be_success_message(self):
        # метод проверки отсутствия сообщения об успешно добавлении в корзину. Метод упадет, как только увидит
        # искомый элемент. Не появился: успех, тест зеленый.
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET), "Success message is " \
                                                                                                  "presented, " \
                                                                                                  "but should not be "

    def should_not_be_success_message_disappeared(self):
        # Метод проверки отсутствия сообщения об успешном добавлении в корзину. Метод будет ждать до тех пор,
        # пока элемент не исчезнет. В противном случае выведет сообщение об ошибке.
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS_ADDED_TO_BASKET), "Success message is " \
                                                                                          "presented, " \
                                                                                          "but should not be "
