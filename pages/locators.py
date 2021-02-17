from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = 'login'


class ProductPageLocators():
    # определяем кортежи для нахождения кнопки добавить в корзину, имени продукта, цены продукта, сообщения об
    # успешном добавлении продукта в корзину, сообщения о соответствии цене корзины, имени продукта в сообщении об
    # успешном добавлении продукта в корзину, общей стоимости корзины после добавления продукта
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    MESSAGE_SUCCESS_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.alert-success.fade.in:nth-child(1) div")
    MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, "div.alert-info.fade.in p:nth-child(1)")
    PRODUCT_NAME_IN_MESSAGE_SUCCESS_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.alert-success.fade.in:nth-child(1) strong")
    PRODUCT_PRICE_IN_MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, "div.alert-info.fade.in strong")


class BasketPageLocators():
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p:nth-child(1)")
