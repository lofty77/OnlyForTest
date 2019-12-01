from nose.tools import assert_equal
from funcs import *
import pytest


def test_func1():
    assert_equal(func1(3), 4)


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--headless')
    return chrome_options


def test_open_web(selenium, chrome_options):
    selenium.get('http://www.baidu.com')
