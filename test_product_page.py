from time import sleep
import pytest
from .pages.product_page import ProductPage


# product = "the-shellcoders-handbook_209/?promo=newYear"
# product = "coders-at-work_207/?promo=newYear2019"

def test_guest_can_go_to_catalogue_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_catalogue_page()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue"])
@pytest.mark.parametrize('product', ["/coders-at-work_207"])
@pytest.mark.parametrize('promo', [
                                    "/?promo=offer0",
                                    "/?promo=offer1",
                                    "/?promo=offer2",
                                    "/?promo=offer3",
                                    "/?promo=offer4",
                                    "/?promo=offer5",
                                    "/?promo=offer6",
                                    "/?promo=offer7",
                                    "/?promo=offer8",
                                    "/?promo=offer9"
                                ])
def test_guest_can_add_product_to_basket(browser, link, product, promo):
    page = ProductPage(browser, link, product, promo)
    page.open()
    page.should_be_add_cart_button()
    page.should_be_correct_item(item="207")
    page.add_item_to_cart(item="207")
    page.solve_quiz_and_get_code()
    pass
    # page.should_be_correct_item_name(item="207")
    # page.should_be_correct_item_price(item="207")
    # page.should_be_correct_item_price(item="207")
