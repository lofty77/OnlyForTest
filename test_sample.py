from nose.tools import assert_equal
from funcs import *
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


def test_func1():
    assert_equal(func1(3), 4)


def test_assert_title_of_homepage():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()

    driver.get("http://automationpractice.com/index.php")
    time.sleep(3)
    login_btn = driver.find_element_by_class_name("login")
    login_btn.click()
    time.sleep(3)
    footer_box_link = driver.find_element_by_xpath("//ul[@class='bullet']")
    footer_link = footer_box_link.find_elements_by_tag_name("li")
    assertEqual(4, len(footer_link))

    driver.quit()


# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.add_argument('--headless')
#     return chrome_options


# def test_open_web(selenium, chrome_options):
#     selenium.get('http://www.baidu.com')
