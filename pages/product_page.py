from .base_page import BasePage
from .locators import PromoPageLocators


class ProductPage(BasePage):

    # def should_be_product_page(self):
    #     self.should_be_product_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()

    # def should_be_correct_item(self):
    #     pass

    def should_be_catalogue_page(self):
        # реализуйте проверку на корректный url адрес
        assert "catalogue" in self.browser.current_url

    def should_be_product_page(self, product, promo=""):
        # реализуйте проверку на корректный url адрес
        assert str(product + promo) in self.browser.current_url

    def should_be_add_cart_button(self):
        assert self.is_element_present(*PromoPageLocators.CART_BUTTON)

    def should_be_correct_item(self, item):
        assert self.is_element_present(*PromoPageLocators.page_item(item))

    def add_item_to_cart(self, item):
        self.click(*PromoPageLocators.page_item(item))
        
    def should_be_correct_price(self, item):
        assert self.is_element_present(*PromoPageLocators.price_item(item))
