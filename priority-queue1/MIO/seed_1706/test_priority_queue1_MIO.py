#Pyguin test cases converted from priority-queue1/MIO/seed_1706/test_priority_queue1.py
import pytest
import priority_queue1 as module_0

def test_case_0():
    none_type_0 = None
    priority_queue_0 = module_0.PriorityQueue()
    assert len(module_0.PriorityQueue.mapper) == 7
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
    var_0 = priority_queue_0.add_task(none_type_0)
    assert len(module_0.PriorityQueue.mapper) == 8

def test_case_1():
    str_0 = '$05`KUX 2E4]p%g5'
    priority_queue_0 = module_0.PriorityQueue()
    assert len(module_0.PriorityQueue.mapper) == 8
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
    var_0 = priority_queue_0.add_task(str_0)
    assert len(module_0.PriorityQueue.mapper) == 9

def test_case_2():
    none_type_0 = None
    priority_queue_0 = module_0.PriorityQueue()
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
    priority_queue_0.set_priority(none_type_0, priority_queue_0)

def test_case_3():
    none_type_0 = None
    priority_queue_0 = module_0.PriorityQueue()
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
    priority_queue_0.set_priority(none_type_0, none_type_0)

def test_case_4():
    none_type_0 = None
    priority_queue_0 = module_0.PriorityQueue()
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
    priority_queue_0.pop_task()
    priority_queue_1 = module_0.PriorityQueue()
    var_0 = priority_queue_1.set_priority(none_type_0)
    var_1 = priority_queue_0.remove_task(none_type_0)

def test_case_5():
    none_type_0 = None
    priority_queue_0 = module_0.PriorityQueue()
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
    priority_queue_1 = module_0.PriorityQueue()
    var_0 = priority_queue_1.pop_task()
    assert len(module_0.PriorityQueue.mapper) == 7

def test_case_6():
    priority_queue_0 = module_0.PriorityQueue()
    assert len(module_0.PriorityQueue.mapper) == 7
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
    with pytest.raises(KeyError):
        priority_queue_0.pop_task()

def test_case_7():
    priority_queue_0 = module_0.PriorityQueue()
    assert module_0.PriorityQueue.pq == []
    assert len(module_0.PriorityQueue.mapper) == 7
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
    with pytest.raises(KeyError):
        priority_queue_0.pop_task()

def test_case_8():
    priority_queue_0 = module_0.PriorityQueue()
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'

def test_case_9():
    str_0 = ''
    priority_queue_0 = module_0.PriorityQueue()
    assert module_0.PriorityQueue.pq == []
    assert len(module_0.PriorityQueue.mapper) == 7
    assert module_0.PriorityQueue.REMOVED == '__removed-task__'
