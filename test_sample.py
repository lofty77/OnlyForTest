from nose.tools import assert_equal


def func(x):
    return x + 1


def test_func():
    assert_equal(func(3), 4)
