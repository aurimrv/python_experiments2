#Pyguin test cases converted from priority-queue2/DYNAMOSA/seed_1706/test_priority_queue2.py
import pytest
import priority_queue2 as module_0

def test_case_0():
    priority_q_0 = module_0.PriorityQ()
    priority_q_1 = module_0.PriorityQ()
    var_0 = priority_q_0.insert(priority_q_1)
    var_1 = priority_q_0.pop()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'priority_queue2.PriorityQ'
    var_2 = var_1.peek()

def test_case_1():
    priority_q_0 = module_0.PriorityQ()
    var_0 = priority_q_0.peek()
    binheap_0 = priority_q_0.peek()
    priority_q_1 = module_0.PriorityQ()
    none_type_0 = None
    var_1 = priority_q_0.insert(none_type_0)
    priority_q_2 = module_0.PriorityQ()

def test_case_2():
    priority_q_0 = module_0.PriorityQ()
    priority_q_1 = priority_q_0.peek()

def test_case_3():
    priority_q_0 = module_0.PriorityQ()
    priority_q_1 = module_0.PriorityQ()

def test_case_4():
    str_0 = '3\rC\t-OY\n;[Dz\\Y;<-K'
    priority_q_0 = module_0.PriorityQ()
    var_0 = priority_q_0.insert(str_0)
    priority_q_1 = module_0.PriorityQ()
    var_1 = priority_q_1.insert(str_0)
    priority_q_2 = module_0.PriorityQ()
