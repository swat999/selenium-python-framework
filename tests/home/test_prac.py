import pytest_check as check


def test_example():
    a = 1
    b = 2
    c = [2, 4, 6]
    check.greater(a, b)
    check.less_equal(b, a)
    check.is_in(a, c, "Is 1 in the list")
    check.is_not_in(b, c, "make sure 2 isn't in list")