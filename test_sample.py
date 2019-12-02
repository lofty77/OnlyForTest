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
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://www.engagespark.com/")
    assert browser.title == "Home - Send and Receive Automated Call and SMS Text Campaigns."


# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.add_argument('--headless')
#     return chrome_options


# def test_open_web(selenium, chrome_options):
#     selenium.get('http://www.baidu.com')
