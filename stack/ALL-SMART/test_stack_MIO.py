#Pyguin test cases converted from stack/MIO/seed_1706/test_stack.py
import stack as module_0
import pytest

@pytest.mark.xfail(strict=True)
def test_case_0():
    stack_0 = module_0.Stack()
    stack_0.pop()

@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    dict_0 = {}
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(dict_0)
    stack_1 = module_0.Stack(list_0)
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack(stack_2)
    var_1 = stack_3.push(stack_2)
    var_2 = stack_2.push(stack_2)
    var_2.search(stack_2)
