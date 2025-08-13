import pytest
from shipping import is_shipping_free

def test_prime_always_free():
    assert is_shipping_free(5, 1, True) == True

def test_price_boundary_free():
    assert is_shipping_free(50, 1, False) == True
    assert is_shipping_free(25, 3, False) == True
    assert is_shipping_free(10, 1, True) == True

def test_price_boundary_not_free():
    assert is_shipping_free(9.99, 1, False) == False
    assert is_shipping_free(25, 2, False) == False

def test_number_of_items_zero():
    assert is_shipping_free(100, 0, False) == True  # Price rule

def test_branch_c_false():
    assert is_shipping_free(20, 2, False) == False
