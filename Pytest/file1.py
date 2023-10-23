import pytest, file2

from file2 import TestAddNumbers
from file2 import TestAddNumbers

def add_num(a, b):
    return a + b

class TestEverything:
    def __init__(self):
        self.test_add_numbers_with_negative()
        self.test_add_numbers()
        self.test_add_numbers_with_large_numbers()

    def test_add_numbers_with_negative(self):        
        result = add_num(-1, -2)
        assert result == -3
        print(f"Assertion passed: {result} == -3")

    def test_add_numbers(self):
        if hasattr(TestAddNumbers, "test_add_numbers"):
            test = TestAddNumbers()
            test.test_add_numbers(1,2,3)

    def test_add_numbers_with_large_numbers(self):
        if hasattr(TestAddNumbers, "test_add_numbers_with_large_numbers"):
            test = TestAddNumbers()
            test.test_add_numbers_with_large_numbers()

a = TestEverything()