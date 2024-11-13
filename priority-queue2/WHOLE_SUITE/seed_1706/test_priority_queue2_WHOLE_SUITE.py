#Pyguin test cases converted from priority-queue2/WHOLE_SUITE/seed_1706/test_priority_queue2.py
import pytest
import priority_queue2 as module_0
import binheap as module_1

def test_case_0():
    priority_q_0 = module_0.PriorityQ()
    var_0 = priority_q_0.insert(priority_q_0)
    var_1 = priority_q_0.pop()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'priority_queue2.PriorityQ'
    var_2 = priority_q_0.insert(var_0, priority_q_0)

def test_case_1():
    priority_q_0 = module_0.PriorityQ()

def test_case_2():
    binheap_0 = module_1.Binheap()

def test_case_3():
    priority_q_0 = module_0.PriorityQ()
    bool_0 = True
    list_0 = [priority_q_0, priority_q_0, priority_q_0, bool_0]
    none_type_0 = None
    var_0 = priority_q_0.insert(list_0, none_type_0)

def test_case_4():
    priority_q_0 = module_0.PriorityQ()
    var_0 = priority_q_0.peek()

def test_case_5():
    binheap_0 = module_1.Binheap()
    priority_q_0 = module_0.PriorityQ()
    none_type_0 = None
    priority_q_1 = module_0.PriorityQ()
    var_0 = priority_q_1.insert(none_type_0, priority_q_1)

def test_case_6():
    binheap_0 = module_1.Binheap()
    var_0 = binheap_0.display()

def test_case_7():
    priority_q_0 = module_0.PriorityQ()
    var_0 = priority_q_0.peek()
