from hello import add, sub

def test_add():
    assert 2 == add(1, 1)

def test_sub():
    assert 1 == sub(2, 1)
