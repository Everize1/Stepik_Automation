from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def should_be_empty_cart(self):
        assert self.is_not_element_present(*BasePageLocators.CART_CONTENT), "Cart content is not empty"
        assert self.is_element_present(*BasePageLocators.CART_EMPTY_TEXT), "Did not found empty cart message"
