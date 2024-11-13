#Pyguin test cases converted from queue/MOSA/seed_1706/test_a_queue.py
import pytest
import a_queue as module_0

def test_case_0():
    queue_0 = module_0.Queue()
    var_0 = queue_0.peek()

def test_case_1():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)

def test_case_2():
    queue_0 = module_0.Queue()
    var_0 = queue_0.size()
    bool_0 = False
    queue_1 = module_0.Queue(bool_0)
    queue_2 = module_0.Queue(bool_0)

def test_case_3():
    queue_0 = module_0.Queue()
    var_0 = queue_0.peek()
    queue_1 = module_0.Queue()
    var_1 = queue_1.size()
