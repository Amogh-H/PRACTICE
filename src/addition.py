# This is to check and run actions

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, 0) == 1  # Corrected 
