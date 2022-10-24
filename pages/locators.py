from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//*[@id='login_link']")

class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//*[@id='login_link']")
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//*[@id='register_form']")
    