from project import add, sub, mul, rem, div, pow


def testAdd():
    assert add(1,3) == 4
    assert add(2,2) == 4
def testSub():
    assert sub(2,1) == 1
    assert sub(3,2) == 1
def testMul():
    assert mul(2,2) == 4
    assert mul(3,2) == 6
def testPow():
    assert pow(2,2) == 4
    assert pow(3,3) == 27
def testDiv():
    assert div(4,2) == 2
    assert div(6,2) == 3
def testRem():
    assert rem(5,2) == 1
    assert rem(12,5) == 2
    assert rem(245,3) == 2