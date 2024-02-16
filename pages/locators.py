from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_TO_BASKET_PAGE = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE_SM = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME_SM = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".row h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators:
    EMPTY_BASKET_STRING = (By.CSS_SELECTOR, "#content_inner p")
    TOTAL_ORDER = (By.CSS_SELECTOR, "#basket_totals")
    WRITING_EMPTY_BASKET = (By.XPATH, "//p[text()='Ваша корзина пуста']")
