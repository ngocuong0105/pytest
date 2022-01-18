import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []

# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)
# Sometimes you may want to have a fixture (or even several) that you know all your tests will depend on. 
# “Autouse” fixtures are a convenient way to make all tests automatically request them.
@pytest.fixture(autouse=True)
def append_second(order, first_entry):
    return order.append(first_entry)

# return value of order was cached (along with any side effects executing it may have had) 
# append_first fixture has been requested and ran
def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]
