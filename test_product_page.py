import pytest
from .pages.product_page import ProductPage



@pytest.mark.need_review
@pytest.mark.parametrize('promo', [
    "?promo=offer0",
    "?promo=offer1",
    "?promo=offer2",
    "?promo=offer3",
    "?promo=offer4",
    "?promo=offer5",
    "?promo=offer6",
    pytest.param("?promo=offer7", marks=pytest.mark.xfail),
    "?promo=offer8",
    "?promo=offer9"
])
@pytest.mark.parametrize('item', ["coders-at-work_207/"])
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/"])
def test_guest_can_add_product_to_basket(browser, link, item, promo, timeout=4):

    # item - адрес конкретного товара в каталоге -> some-book_id/
    # promo - параметр url для промоакции

    page = ProductPage(browser, link, item, promo, timeout)
    page.open()
    page.should_be_page_element("CART_BUTTON")
    page.should_be_page_element("PAGE_ITEM_NAME")
    page.should_be_page_element("PAGE_ITEM_PRICE")

    exp_item_id = page.get_item_id_from_url(item)
    exp_item_name = page.get_item_name_from_url(item)
    exp_item_price = page.get_item_price().text

    page.add_item_to_cart(exp_item_id)
    page.solve_quiz_and_get_code()

    # вытащить текст алертов после добавления в корзину
    alerts_elements = page.get_item_alerts_after_add()
    page.should_contain_expected_name(
        exp_item_name, alerts_elements[0].text.lower())
    page.should_contain_expected_price(
        exp_item_price, alerts_elements[-1].text)


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/"])
@pytest.mark.parametrize('item', ["coders-at-work_207/"])
class TestProductSuccessMessageAfterAdding:
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link, item):
        page = ProductPage(browser, link, item)
        page.open()
        page.add_item_to_cart(exp_item_id=page.get_item_id_from_url(item))
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, link, item):
        page = ProductPage(browser, link, item)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link, item):
        page = ProductPage(browser, link, item)
        page.open()
        page.add_item_to_cart(exp_item_id=page.get_item_id_from_url(item))
        page.is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser, link, item):
        page = ProductPage(browser, link, item)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link, item):
        page = ProductPage(browser, link, item)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link, item):
        page = ProductPage(browser, link, item)
        page.open()
        page.click_on_open_cart_button()
        page.should_be_empty_cart()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/"])
@pytest.mark.parametrize('item', ["coders-at-work_207/"])
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        from .pages.login_page import LoginPage
        link_register = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link=link_register)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link, item):
        page = ProductPage(browser, link, item, timeout=10)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link, item):
        
        # item - адрес конкретного товара в каталоге -> some-book_id/
        # promo - параметр url для промоакции
        page = ProductPage(browser, link, item)
        page.open()
        page.should_be_page_element("CART_BUTTON")
        page.should_be_page_element("PAGE_ITEM_NAME")
        page.should_be_page_element("PAGE_ITEM_PRICE")
        exp_item_id = page.get_item_id_from_url(item)
        exp_item_name = page.get_item_name_from_url(item)
        exp_item_price = page.get_item_price().text
        page.add_item_to_cart(exp_item_id)

        # вытащить текст алертов после добавления в корзину
        alerts_elements = page.get_item_alerts_after_add()
        page.should_contain_expected_name(
            exp_item_name, alerts_elements[0].text.lower())
        page.should_contain_expected_price(
            exp_item_price, alerts_elements[-1].text)
