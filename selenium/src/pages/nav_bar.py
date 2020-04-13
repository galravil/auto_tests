from .base import BasePage
from selenium.webdriver.common.by import By


class NavBarSelectors:
    SEL_HOME = (By.CSS_SELECTOR, '.nav-item :nth-child(0)')
    SEL_SIGN_IN = (By.CSS_SELECTOR, '.nav-item :nth-child(1)')
    SEL_SIGN_UP = (By.CSS_SELECTOR, '.nav-item :nth-child(2)')


class NavBar(BasePage):
    def click_on_home(self):
        element = self.find_element(NavBarSelectors.SEL_HOME)
        return element.click()
    
    def click_on_sign_in(self):
        element = self.find_element(NavBarSelectors.SEL_SIGN_IN)
        return element.click()
    
    def click_on_sign_up(self):
        element = self.find_element(NavBarSelectors.SEL_SIGN_UP)
        return element.click()
