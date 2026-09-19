from hints import parity, n_range, divisible

def test_parity_even():
    assert parity(10) == "The number is even."

def test_parity_odd():
    assert parity(7) == "The number is odd."

def test_n_range_low():
    assert n_range(15) == "The number is between 1 and 25"

def test_n_range_high():
    assert n_range(90) == "The number is between 76 and 100"

def test_divisible_by_3():
    assert divisible(9) == "The number is divisible by 3."

def test_divisible_none():
    assert divisible(11) == "The number is not divisible by 3, 5, or 7."