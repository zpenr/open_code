import sys
sys.path.append("../src")

from math_demo import add, add_with_bug

def test_addtional():
    assert add(2,2) == 4
    print("Test ADDITIONAL PASSED")

def test_addtional_with_bug():
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    print("Test BUG ADDITIONAL PASSED (it's ok?)")

if __name__ == "__main__":
    test_addtional()
    test_addtional_with_bug()

