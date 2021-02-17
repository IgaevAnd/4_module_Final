from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        # is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Basket is not empty, but should be"

    def should_be_message_basket_empty(self):
        # is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), "There is no message stating that " \
                                                                                  "the cart is empty, but should be "

