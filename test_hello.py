from hello import add, sub, mult

def test_add():
    assert 2 == add(1, 1)

def test_sub():
    assert 1 == sub(2, 1)

def test_mult():
    assert 6 == mult(3, 2)
