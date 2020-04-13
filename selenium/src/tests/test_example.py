import os
import pytest
from selenium import webdriver
from selenium.webdriver.common import by
import time

from ..data.urls import URLS
from ..data.users import BaseUser
from ..pages.sign_in import LogInPage
from ..pages.feed_toggle import FeedToggle
from ..pages.article_list import ArticleList


def test_base_page(driver):
    driver.get(URLS.home)
    assert driver.current_url == URLS.home

def test_login(driver):
    login = LogInPage(driver)
    login.go_to_page()
    login.fill_in_form(BaseUser.email, BaseUser.password)
    time.sleep(2)
    assert driver.current_url == URLS.home


def test_feeds(driver):
    login = LogInPage(driver)
    login.go_to_page()
    login.fill_in_form(BaseUser.email, BaseUser.password)
    time.sleep(2)
    assert driver.current_url == URLS.home

    # your feeds
    feed_toggle = FeedToggle(driver)
    feed_toggle.click_on_my_feed()

    article_list = ArticleList(driver)
    article_list.check_empty_article_list()

    # global feeds
    feed_toggle.click_on_global_feed()
    time.sleep(2)
    
    article_list.check_article_list()
