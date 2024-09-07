# test_function_module.py

from cityu_pack.sub_func_pack.func_module import add, multiply

def test_add():
    assert add(1, 2) == 3

def test_multiply():
    assert multiply(2, 3) == 6
