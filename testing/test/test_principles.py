import sys
sys.path.append("../src")

from math_demo import add

def test_addtional():
    assert add(2,2) == 4
    print("Test complite")

if __name__ == "__main__":
    test_addtional()

