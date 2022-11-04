from .base_page import BasePage
from .locators import ProductPageLocators
import re


class ProductPage(BasePage):

    # вытащить из адреса ID товара
    def get_item_id_from_url(self, item):
        item_id = re.search(r"[\d]+", item).group()
        return item_id

    # вытащить из адреса NAME товара
    def get_item_name_from_url(self, item):
        item_name = re.findall(r"[a-z]+", item)
        return " ".join(item_name).lower()

    # провека что элемент об успешном добавлении элемента отсутствует
    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is shown on the page"

    # провека что элемент страницы товара присутствует
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

    # вытащить стоимость товара
    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.PAGE_ITEM_PRICE)

    # Найти и нажать на кнопку добавления товара по ID
    def add_item_to_cart(self, item_id):
        assert self.is_element_present(
            *ProductPageLocators.get_basket_add_button_by_xpath_locator_with_id(item_id)), "Did not found item by id"
        self.click(
            *ProductPageLocators.get_basket_add_button_by_xpath_locator_with_id(item_id))

    # собрать элементы
    def get_item_alerts_after_add(self):
        return self.browser.find_elements(*ProductPageLocators.ADD_ITEM_ALERTS)

    # сравнить название товара
    def should_contain_expected_name(self, exp_element, act_element):
        assert exp_element == act_element, "Expected item NAME is not the same as described on the page"

    # сравнить цену товара
    def should_contain_expected_price(self, exp_element, act_element):
        assert exp_element == act_element, "Expected item PRICE is not the same as described on the page"
