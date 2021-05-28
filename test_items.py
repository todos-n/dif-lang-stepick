import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link = "https://stepik.org/"
#для теста с отсутствием кнопки

def test_find_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    #таймер для визуальной оценки используемого языка и результата
    button = None
    try:
        button = browser.find_element_by_class_name("btn-add-to-basket")       
    finally:
        assert button != None, "Should be 'add to basket' button"

