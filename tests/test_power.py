from src.power import power


def test_power_basic():
    # Regular integer powers
    assert power(2, 3) == 8
    assert power(5, 1) == 5
    assert power(10, 2) == 100


def test_power_with_zero():
    # Zero exponents and bases
    assert power(5, 0) == 1          # anything^0 = 1
    assert power(0, 5) == 0          # 0^positive = 0
    assert power(0, 0) == 1          # Python defines 0**0 as 1


def test_power_negative_exponent():
    # Negative exponents → reciprocal
    assert power(2, -2) == 0.25
    assert power(10, -1) == 0.1


def test_power_fractional_exponent():
    # Fractional powers → roots
    assert power(9, 0.5) == 3
    assert round(power(27, 1/3), 5) == 3  


def test_power_negative_base():
    # Negative bases
    assert power(-2, 3) == -8
    assert power(-2, 2) == 4
