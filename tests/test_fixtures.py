# test_fixtures.py

import pytest

# before each test
@pytest.fixture
def numbers(): # this can be input directly into test methods and is built like a function
    a = 10
    b = 20
    c = 25
    return [a,b,c]

# this one failed
@pytest.mark.xfail
def test_method1(numbers):
    x = 15
    assert numbers[0] == x


# skip this one
@pytest.mark.skip
def test_method2(numbers):
    y = 20
    assert numbers[1] == y
    
def test_method3(numbers):
    z = 25
    assert numbers[2] == z
    
# these marks make sure it doesn't show failed when running pytest, shows skipped and xfailed