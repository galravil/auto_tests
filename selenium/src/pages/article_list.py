from .base import BasePage
from selenium.webdriver.common.by import By


class ArticleListSel:
    SEL_ARTICLE_EMPTY_LIST = (By.CSS_SELECTOR, 'div.article-preview')
    text_if_no_articles = 'No articles are here... yet.'
    SEL_ARTICLE = (By.CSS_SELECTOR, 'div.article-preview')

class ArticleList(BasePage):
    def check_empty_article_list(self):
        element = self.find_element(ArticleListSel.SEL_ARTICLE_EMPTY_LIST)
        assert ArticleListSel.text_if_no_articles in element.text, 'Article list is not empty'
        return element
    
    def check_article_list(self):
        elements = self.find_elements(ArticleListSel.SEL_ARTICLE)

        assert len(elements) == 10
        return elements
