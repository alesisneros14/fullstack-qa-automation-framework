from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class LoginPage(BasePage):
    # LOCALIZADORES
    USER_INPUT = (By.ID, "username")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    WELCOME_MSG = (By.ID, "welcome-msg")
    ERROR_MSG = (By.ID, "error-msg")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://localhost:5000" # URL de tu app local

    def open(self):
        self.driver.get(self.url)

    def perform_login(self, user, password):
        self.type_text(self.USER_INPUT, user)
        self.type_text(self.PASS_INPUT, password)
        self.click(self.LOGIN_BTN)

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MSG)
        
    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)