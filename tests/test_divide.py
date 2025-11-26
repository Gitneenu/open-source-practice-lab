from src.divide import divide
import pytest

def test_divide():
    assert divide(8, 2) == 4

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)
