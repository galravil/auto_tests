from selenium.webdriver.common.by import By
from .base import BasePage
from ..data.urls import URLS


class LogInSelectors:
    SEL_LOGIN_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    SEL_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    SEL_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.pull-xs-right')


class LogInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = URLS.login

    def fill_in_email(self, email):
        el = self.find_element(LogInSelectors.SEL_LOGIN_INPUT)
        return el.send_keys(email)

    def fill_in_password(self, password):
        el = self.find_element(LogInSelectors.SEL_PASSWORD_INPUT)
        return el.send_keys(password)

    def submit_form(self):
        el = self.find_element(LogInSelectors.SEL_SUBMIT_BUTTON)
        return el.click()

    def fill_in_form(self, email, password):
        self.fill_in_email(email)
        self.fill_in_password(password)
        self.submit_form()
        return (email, password)
