from tkinter import S
import pytest

def f():
    raise SystemExit(1) # Python raise Keyword is used to raise exceptions or errors. The raise keyword raises an error and stops the control flow of the program.

def test_mytest():
    with pytest.raises(SystemExit):
        f()
#%%
'''
The sys.exit() function allows the developer to exit from Python. 
The exit function takes an optional argument, typically an integer, that gives an exit status. Zero is considered a “successful termination”. 
'''
import sys
print(1)
# raise SystemExit(69)
sys.exit(69)
print(2)
# sys.exit(s) is just shorthand for raise SystemExit(s)
