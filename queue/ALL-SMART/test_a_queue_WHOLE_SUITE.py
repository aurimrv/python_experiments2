#Pyguin test cases converted from queue/WHOLE_SUITE/seed_1706/test_a_queue.py
import pytest
import a_queue as module_0
import dll as module_1

def test_case_0():
    queue_0 = module_0.Queue()
    var_0 = queue_0.size()
    var_1 = queue_0.enqueue(queue_0)
    bool_0 = True
    tuple_0 = (bool_0, var_0)

def test_case_1():
    tuple_0 = ()
    none_type_0 = None
    queue_0 = module_0.Queue(tuple_0)
    var_0 = queue_0.size()
    set_0 = {tuple_0, none_type_0, var_0, var_0}
    var_1 = queue_0.enqueue(set_0)
    var_2 = queue_0.enqueue(none_type_0)
    queue_1 = module_0.Queue(tuple_0)
    var_3 = queue_1.size()

def test_case_2():
    queue_0 = module_0.Queue()
    var_0 = queue_0.peek()

def test_case_3():
    queue_0 = module_0.Queue()
    var_0 = queue_0.peek()
    var_1 = queue_0.size()

def test_case_4():
    str_0 = '2"wU\'\x0c"Z3`3G66[vUW'
    set_0 = {str_0, str_0, str_0, str_0}
    bytes_0 = b'\x15\x87\xd7\xdd\xa5\x99M`\xab\xa6\xe4KY\xb2\x8f\x8f\xd4'
    bool_0 = True
    queue_0 = module_0.Queue(set_0)
    queue_1 = module_0.Queue()
    complex_0 = -1111 + 1510.263j
    var_0 = queue_0.peek()
    tuple_0 = (bytes_0, bool_0, complex_0, bool_0)
    var_1 = queue_0.peek()
    var_2 = queue_0.size()
    queue_2 = module_0.Queue(tuple_0)
    var_3 = queue_2.size()
    var_4 = queue_2.dequeue()
    complex_1 = 2621.233 + 4019.72685j

def test_case_5():
    double_linked_list_0 = module_1.DoubleLinkedList()
    int_0 = 741
    queue_0 = module_0.Queue(int_0)
    var_0 = queue_0.peek()

def test_case_6():
    queue_0 = module_0.Queue()
    none_type_0 = None
    var_0 = queue_0.enqueue(none_type_0)
    var_1 = queue_0.dequeue()

def test_case_7():
    queue_0 = module_0.Queue()
    var_0 = queue_0.size()
