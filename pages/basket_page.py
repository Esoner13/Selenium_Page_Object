from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.TOTAL_ORDER), "Basket is not empty"

    def should_be_empty_basket_string(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_STRING), "Empty basket string is not presented"
        empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_STRING)
        eb = empty_basket.text
        assert "Your basket is empty. Continue shopping" == eb




