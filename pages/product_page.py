from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_link.click()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not same"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name = product_name.text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_SM)
        nim = name_in_message.text
        assert name == nim, "Name is wrong"

    def should_be_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Basket price is not same"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price = product_price.text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_SM)
        pim = price_in_message.text
        assert price == pim, "Price is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message presented"
