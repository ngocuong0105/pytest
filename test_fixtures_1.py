import pytest

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

# We can tell pytest that a particular function is a fixture by decorating it with @pytest.fixture.
@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket():
    return [Fruit("banana"),Fruit("apple")]

# Fixtures can request other fixtures
@pytest.fixture
def fruit_basket1(my_fruit):
    return [my_fruit]

def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
    assert my_fruit in fruit_basket1
