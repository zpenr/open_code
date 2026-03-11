from ndfl import calculate_ndfl_tax

def test_ndfl_tier1():
    assert calculate_ndfl_tax(500_000) == 65_000


def test_ndfl_tier2():
    assert calculate_ndfl_tax(4_000_000) == 552_000


def test_ndfl_tier3():
    assert calculate_ndfl_tax(10_000_000) == 1_602_000