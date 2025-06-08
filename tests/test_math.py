from mymodule.math import add, sub

def test_add():
    assert add(2, 4) == 6

def test_sub():
    assert sub(2, 0) == 2
