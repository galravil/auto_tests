from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from ..data.urls import URLS

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.page_url = URLS.home
    
    def find_element(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            ES.presence_of_element_located(selector),
            message=f"Can't find element by selector {selector}"
        )

    def find_elements(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            ES.presence_of_all_elements_located(selector),
            message=f"Can't find elements by selector {selector}"
        )
    
    def go_to_page(self):
        print(self.page_url)
        return self.driver.get(self.page_url)
