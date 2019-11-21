from nose.tools import assert_equal


def func1(x):
    return x + 1


def func2(x):
    return x * x


def func3(x):
    return 2 * x


def test_func1():
    assert_equal(func1(3), 4)
