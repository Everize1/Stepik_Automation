from .base_page import BasePage
from .locators import ProductPageLocators
import re


class ProductPage(BasePage):

    # TODO: сделать проверку что страница корректная

    def get_item_id_from_url(self, item):  # вытащить из адреса ID товара
        item_id = re.search(r"[\d]+", item).group()
        return item_id

    def get_item_name_from_url(self, item):  # вытащить из адреса NAME товара
        item_name = re.findall(r"[a-z]+", item)
        return " ".join(item_name).lower()

    def should_be_page_element(self, page_element):
        if page_element == "CART_BUTTON":
            assert self.is_element_present(
                *ProductPageLocators.CART_BUTTON)
        elif page_element == "PAGE_ITEM_NAME":
            assert self.is_element_present(
                *ProductPageLocators.PAGE_ITEM_NAME)
        elif page_element == "PAGE_ITEM_PRICE":
            assert self.is_element_present(
                *ProductPageLocators.PAGE_ITEM_PRICE)

    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.PAGE_ITEM_PRICE)

    def add_item_to_cart(self, item_id):
        self.click(*ProductPageLocators.get_basket_add_by_xpath_locator(item_id))

    def get_item_alerts_after_add(self):
        return self.browser.find_elements(*ProductPageLocators.ADD_ITEM_ALERTS)

    def should_contain_expected_text(self, exp_element, act_element):
        if exp_element == act_element:
            return True
        else:
            return False
