import pytest

def func(x):
    return x*2

@pytest.mark.one
def test_answer1():
    assert func(2) == 4

@pytest.mark.two
def test_answer2():
    assert func(3) == 6

# Next is equivalent to directly applying the decorator to the all test functions.

@pytest.fixture
def input():
    return [3,2]
@pytest.mark.webtest
class TestClass:

    @classmethod
    def setup_class(cls):
        cls.var1 = 2

    def func(x):
        return x*2

    def test_answer1(self):
        assert func(self.var1) == 4
    
    def test_answer2(input):
        assert func(input[0]) == 4

    def test_startup(self):
        assert 1

    def test_startup_and_more(self):
        pass