import pytest
from calculator.calculator import Calculator


def test_add():
    calculator = Calculator()
    result = calculator.add(15)
    assert result == 15


def test_subtract():
    calculator = Calculator(20)
    result = calculator.subtract(15)
    assert result == 5


def test_multiply():
    calculator = Calculator(2)
    result = calculator.multiply(15)
    assert result == 30


def test_divide():
    calculator = Calculator(50)
    result = calculator.divide(0)
    assert result == 50


def test_nth_root():
    calculator = Calculator(100)
    result = calculator.nth_root(2)
    assert result == 10


def test_reset():
    calculator = Calculator(10)
    result = calculator.reset()
    assert result == 0
