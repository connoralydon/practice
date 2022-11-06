# test_example.py
# needs to start with test_

import pytest

def func(x):
    return x + 5

# this is a testing function
@pytest.mark.one
def test_method1():
    assert func(3) == 5

@pytest.mark.two
def test_method2():
    x = 5
    y = 10
    assert x == y

@pytest.mark.three
def test_method3():
    a = 15
    b = 20
    assert a+5 == b


# command line methods
    # pytest -m two
    # pytest -k method1 -v #




    
    
