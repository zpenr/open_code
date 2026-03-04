import sys

sys.path.append("../src")

from math_demo import add, add_with_bug, calculate_tax_with_bag, calculate_tax

def test_addtional():
    assert add(2,2) == 4
    print("Test ADDITIONAL PASSED")

def test_addtional_with_bug():
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    print("Test BUG ADDITIONAL PASSED (it's ok?)")

def test_additional_duplicate():
    assert add(2,3) == 2 + 3

def test_additional_overcomplicated():
    for i in range(0,2**32):
        for j in range(0,2**32):
            assert add(i,j) == sum([i, j])
            assert add(i,-j) == sum([i, -j])
            assert add(-i,j) == sum([-i, j])
            assert add(-i,-j) == sum([-i, -j])


def test_additional_reasonable():
    assert add(2,2) == 4
    assert add(0,0) == 0
    assert add(6,7) == 13
    assert add(-6,-7) == -13
    assert add(-6,7) == 1
    assert add(-7,0) == -7
    assert add(7,0) == 7

def test_tax_calculate_pesticised():
    assert calculate_tax_with_bag(1000) == 150.0
    assert calculate_tax_with_bag(-1000) == -150.0
    assert calculate_tax_with_bag(10) == 1.5
    assert calculate_tax_with_bag(1) == 0.15
    assert calculate_tax_with_bag(0) == 0.
    print("Test TAX CALCULATION PESTICISED PASSED")
    # must fails with float
    # assert calculate_tax_with_bag(24.5) == 3.67

def test_tax_calculate():
    assert calculate_tax(1000) == 150.0
    assert calculate_tax(-1000) == -150.0
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(0) == 0.
    assert calculate_tax(24.5) == 3.67
    print("Test TAX CALCULATION PASSED")

if __name__ == "__main__": 
    test_addtional()
    test_addtional_with_bug()
    test_additional_duplicate()
    # test_additional_overcomplicated()
    test_additional_reasonable()
    test_tax_calculate_pesticised()
    test_tax_calculate()

