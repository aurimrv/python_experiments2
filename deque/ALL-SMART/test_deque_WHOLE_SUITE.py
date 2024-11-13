#Pyguin test cases converted from deque/WHOLE_SUITE/seed_1706/test_deque.py
import pytest
import dll as module_0
import deque as module_1

def test_case_0():
    none_type_0 = None
    double_linked_list_0 = module_0.DoubleLinkedList()
    var_0 = double_linked_list_0.push(none_type_0)

def test_case_1():
    deque_0 = module_1.Deque()
    var_0 = deque_0.peek()
    var_1 = deque_0.peek()
    deque_1 = module_1.Deque()
    var_2 = deque_1.peek()

def test_case_2():
    none_type_0 = None
    none_type_1 = None
    deque_0 = module_1.Deque(none_type_1)
    var_0 = deque_0.append(none_type_0)
    var_1 = deque_0.size()
    deque_1 = module_1.Deque()
    var_2 = deque_0.peek()

def test_case_3():
    deque_0 = module_1.Deque()
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0}
    deque_1 = module_1.Deque()
    var_0 = deque_1.append(dict_0)

def test_case_4():
    none_type_0 = None
    int_0 = 1746
    deque_0 = module_1.Deque(int_0)
    var_0 = deque_0.append(none_type_0)

def test_case_5():
    deque_0 = module_1.Deque()

def test_case_6():
    deque_0 = module_1.Deque()
    none_type_0 = None
    var_0 = deque_0.appendleft(deque_0)
    var_1 = deque_0.peekleft()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'deque.Deque'
    var_2 = deque_0.peek()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'deque.Deque'
    var_3 = deque_0.pop()
    var_4 = deque_0.size()
    var_5 = deque_0.size()
    var_6 = deque_0.appendleft(none_type_0)
    var_7 = deque_0.size()

def test_case_7():
    deque_0 = module_1.Deque()
    var_0 = deque_0.peekleft()
