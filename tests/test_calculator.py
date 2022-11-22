"""test for our calculator module"""
import pytest

from src.calculator import addIntegers, subtractIntegers

num1: int = 10
num2: int = 5

def test_add_numbers() -> None:
    """Testing adding integers"""
    assert addIntegers(num1, num2) == 15

def test_subtract_numbers() -> None:
    """Testing subtracting integers"""
    assert subtractIntegers(num1, num2) == 5
    