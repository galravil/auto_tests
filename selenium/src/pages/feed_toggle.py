from .base import BasePage
from selenium.webdriver.common.by import By


class FeedToggleSelectors:
    SEL_GLOBAL_FEED = (By.CSS_SELECTOR, 'ul.nav-pills :nth-child(2) a')
    SEL_MY_FEED = (By.CSS_SELECTOR, 'ul.nav-pills :nth-child(1) a')
    

class FeedToggle(BasePage):
    def click_on_my_feed(self):
        element = self.find_element(FeedToggleSelectors.SEL_MY_FEED)
        return element.click()
    
    def click_on_global_feed(self):
        element = self.find_element(FeedToggleSelectors.SEL_GLOBAL_FEED)
        return element.click()
