from .base_page import BasePage
from .locators import ProductPageLocators
import re


class ProductPage(BasePage):

    # def should_be_product_page(self):
    #     self.should_be_product_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()

    # TODO: сделать проверку что страница корректная

    # def should_be_correct_item(self):
    #     pass

    # def should_be_catalogue_page(self):
    #     # реализуйте проверку на корректный url адрес
    #     assert "catalogue" in self.browser.current_url

    # def should_be_product_page(self, product, promo=""):
    #     # реализуйте проверку на корректный url адрес
    #     assert str(product + promo) in self.browser.current_url

    def should_be_add_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.CART_BUTTON)

    def get_item_id_from_url(self, item):
        # вытащить из адреса ID товара
        item_id = re.search(r"[\d]+", item).group()
        return item_id

    def get_item_name_from_url(self, item):
        # вытащить из адреса NAME товара
        item_name = re.findall(r"[a-z]+", item)
        return " ".join(item_name).lower()
    
    def get_item_alerts_after_add(self):
        return self.browser.find_elements(*ProductPageLocators.ADD_ITEM_ALERTS)

    # def check_ubtton(self):
    #     assert self.is_element_present(*PromoPageLocators.get_item_id_from_basket_button(item_id))

    def add_item_to_cart(self, item_id):
        self.click(*ProductPageLocators.get_basket_add_by_xpath_locator(item_id))

    def should_be_correct_item_names(self, exp_item_name, act_item_name):
        pass
