from time import sleep
import pytest
from .pages.product_page import ProductPage


# product = "the-shellcoders-handbook_209/?promo=newYear"
# product = "coders-at-work_207/?promo=newYear2019"

# TODO: ПОТОМ

# def test_guest_can_go_to_catalogue_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_catalogue_page()


@pytest.mark.parametrize('promo', [
                                    "?promo=offer0",
                                    "?promo=offer1",
                                    "?promo=offer2",
                                    "?promo=offer3",
                                    "?promo=offer4",
                                    "?promo=offer5",
                                    "?promo=offer6",
                                    "?promo=offer7",
                                    "?promo=offer8",
                                    "?promo=offer9"
                                ])
@pytest.mark.parametrize('item', ["coders-at-work_207/"])
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/"])
def test_guest_can_add_product_to_basket(browser, link, item, promo):
    # item - адрес конкретного товара в каталоге -> some-book_id/
    # promo - параметр url для промоакции
    page = ProductPage(browser, link, item, promo)
    page.open()
    page.should_be_add_cart_button()
    
    exp_item_id = page.get_item_id_from_url(item)
    exp_item_name = page.get_item_name_from_url(item)

    page.add_item_to_cart(exp_item_id)
    page.solve_quiz_and_get_code()
    
    alerts_elements = page.get_item_alerts_after_add()
    
    for i in alerts_elements:
        print(i.text)

    # page.should_be_correct_item_names(exp_item_name, act_item_name)

