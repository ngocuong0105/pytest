### Notes on Pytest library

**pytest** is a framework that makes building simple and scalable tests easy

- pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories


### Commands

- run all test_*.py and *_test.py files:
```
pytest
```
- run in quite mode:
```
pytest -q test_example.py
```

- how to properly assert that an exception gets raised in pytest? Check test_raises.py