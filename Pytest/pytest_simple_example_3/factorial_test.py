from factorial_example import calculate_factorial
import pytest

def test_factorial_positive():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError):
        calculate_factorial(-1)

def test_factorial_non_integer():
    with pytest.raises(ValueError):
        calculate_factorial(3.5)
