from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = 'login'
    ID_NEW_LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    ID_NEW_LOGIN_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    ID_NEW_LOGIN_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():
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
