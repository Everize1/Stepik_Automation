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


class PromoPageLocators():
    def page_item(item):
        return By.XPATH, ("//*[@action='/ru/basket/add/" + str(item) + "/']")
    def price_item(item):
        return By.XPATH, ("//*[@action='/ru/basket/add/" + str(item) + "/']")
    CART_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    ITEM_PRICE = (By.XPATH, "")
    CART_ITEM_ALERT = (By.XPATH, "//*[@=]")
    CART_PRICE = (By.XPATH, "//*[@=]")
