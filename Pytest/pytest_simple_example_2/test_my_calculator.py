"""  
Notes:
The @pytest.fixture decorator can be used to define a fixture function. 
Fixtures are a powerful feature in pytest for setting up and tearing down resources that the test functions need. 
They help in managing the test environment (before running the tests) and provide a clean and organized way to prepare data or perform actions. 
"""
import pytest
from my_calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    result = calculator.add(2, 3)
    assert result == 5

def test_subtraction(calculator):
    result = calculator.subtract(5, 2)
    assert result == 3

def test_multiplication(calculator):
    result = calculator.multiply(4, 3)
    assert result == 12

def test_division(calculator):
    result = calculator.divide(8, 2)
    assert result == 4

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

def test_square(calculator):
    result = calculator.square(4)
    assert result == 16

def test_cube(calculator):
    result = calculator.cube(3)
    assert result == 27

def test_square_root_positive(calculator):
    result = calculator.sqrt(25)
    assert result == 5

def test_square_root_negative(calculator):
    with pytest.raises(ValueError):
        calculator.sqrt(-16)