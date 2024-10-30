"""Test that our modules behaves as expected"""

from mypackage.add_number import add_num


def test_add_num():
    """Test that the add number function is correct"""

    assert add_num(3, 4) == 7
