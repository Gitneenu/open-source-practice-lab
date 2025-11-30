import pytest
from utils import is_number

def test_is_number_positive_integers():
    assert is_number("10") is True
    assert is_number("123456") is True

def test_is_number_negative_integers():
    assert is_number("-5") is True
    assert is_number("-999") is True

def test_is_number_floats():
    assert is_number("3.14") is True
    assert is_number("-2.718") is True
    assert is_number("0.0") is True

def test_is_number_invalid_inputs():
    assert is_number("abc") is False
    assert is_number("") is False
    assert is_number("12a") is False
    assert is_number("3.14.15") is False
