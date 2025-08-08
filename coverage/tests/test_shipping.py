from shipping import is_shipping_free

def test_case_1():
    # is_shipping_free(30,2,True) -> True
    assert is_shipping_free(30,2,True) is True

def test_case_2():
    # is_shipping_free(15,1,False) -> False
    assert is_shipping_free(15,1,False) is False

def test_case_3():
    # is_shipping_free(15,1,True) -> False
    assert is_shipping_free(15,1,True) is False

def test_case_4():
    # is_shipping_free(50,1,False) -> True
    assert is_shipping_free(50,1,False) is True
