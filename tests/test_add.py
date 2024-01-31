from add import add
def test_add():
    assert add(2,2)==4

def test_fail():
    assert add(2,3)==4
