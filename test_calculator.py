# test_calculator.py
import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(0, 5) == -5
    assert calculator.subtract(-3, -1) == -2

def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0, 5) == 0

def test_divide():
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(7, 2) == 3.5
    assert calculator.divide(-6, 2) == -3.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)

def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(4, 0.5) == 2.0
