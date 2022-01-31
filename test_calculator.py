# library import python packages
import logging
import pytest
import sys

# classes import (from packages)
from Calculator import Calculator


def add(input1, input2, expected_result):
    calculator = Calculator()
    result = calculator.add(input1, input2)
    assert result == expected_result


def multiply(input1: int, input2: int, expected_result):
    calculator = Calculator()
    result = calculator.multiply(input1, input2)
    assert result == expected_result


def subtract(input1: int, input2: int, expected_result):
    calculator = Calculator()
    result = calculator.subtract(input1, input2)
    assert result == expected_result


def test_add():
    add(3, 9, 12)
    add(4, 9, 13)
    add(3, 1, 4)
    add(3, 8, 11)


def test_multiply_int():
    multiply(4, 4, 16)


def test_subtract():
    subtract(4, 2, 2)
    subtract(1, 2, -1)
    subtract(1, 0, 1)
    subtract(2, 2, 0)
