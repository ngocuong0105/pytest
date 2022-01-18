import pytest

def func(x):
    return x*2

@pytest.mark.one
def test_answer1():
    assert func(3) == 5

@pytest.mark.two
def test_answer2():
    assert func(3) == 6

# Next is equivalent to directly applying the decorator to the two test functions.
@pytest.mark.webtest
class TestClass:
    def test_startup(self):
        assert 0

    def test_startup_and_more(self):
        pass