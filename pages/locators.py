from selenium.webdriver.common.by import By

""" 

Template:

class __PageLocators():
    _ = (By.XPATH, "//*[@=]")
    
"""


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//*[@id='login_link']")


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//*[@id='login_link']")
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//*[@id='register_form']")


class ProductPageLocators():
    # найти локатор кнопки добавления корзины с совпадающим ID товара
    def get_basket_add_button_by_xpath_locator_with_id(item_id):
        return By.XPATH, (f"//*[@action='/ru/basket/add/{item_id}/']")

    CART_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    PAGE_ITEM_NAME = (By.XPATH, "//*[@class='col-sm-6 product_main']/*[1]")
    PAGE_ITEM_PRICE = (By.XPATH, "//*[@class='col-sm-6 product_main']/*[2]")
    ADD_ITEM_ALERTS = (By.XPATH, "//div[@id='messages']/div//strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")
    
class BasePageLocators():
    
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")