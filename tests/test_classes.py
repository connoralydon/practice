# test_classes.py

import pytest

# using classes
class TestClass:
    def test_one(self):
        x = 'abc'
        assert 'b' in x
        
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")