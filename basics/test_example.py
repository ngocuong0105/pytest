# run pytest is equivalent to
# pytest test_example
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

