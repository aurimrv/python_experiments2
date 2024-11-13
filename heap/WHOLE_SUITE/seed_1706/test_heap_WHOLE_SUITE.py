#Pyguin test cases converted from heap/WHOLE_SUITE/seed_1706/test_heap.py
import pytest
import heap as module_0

def test_case_0():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    bool_0 = True
    var_0 = heap_0.find_min_child_index(bool_0)

def test_case_1():
    bool_0 = True
    bool_1 = True
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.delete_min()
    var_1 = heap_0.insert(bool_1)
    assert heap_0.heap_list == [0, True]
    bool_2 = False
    var_2 = heap_0.insert(bool_2)
    assert heap_0.heap_list == [0, False, True]

def test_case_2():
    bool_0 = True
    bool_1 = True
    bool_2 = False
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.min()
    var_1 = heap_0.insert(bool_2)
    assert heap_0.heap_list == [0, False]
    var_2 = heap_0.insert(bool_0)
    assert heap_0.heap_list == [0, False, True]

def test_case_3():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(heap_0)
    var_1 = heap_0.delete_min()
    assert heap_0.heap_list == [0]
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'heap.Heap'
    assert var_1.heap_list == [0]

def test_case_4():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]

def test_case_5():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.delete_min()

def test_case_6():
    list_0 = []
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.size()
    assert var_0 == 0
    var_1 = heap_0.build(list_0)

def test_case_7():
    int_0 = -2440
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, int_0]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_0 = heap_1.build(list_0)
    assert heap_1.heap_list == [0, -2440, True, True, True, True]
    var_1 = heap_1.delete_min()
    assert var_1 == -2440
    assert heap_1.heap_list == [0, True, True, True, True]
    none_type_0 = None
    heap_2 = module_0.Heap()
    assert heap_2.heap_list == [0]
    var_2 = heap_2.size()
    assert var_2 == 0
    var_3 = heap_0.min()

def test_case_8():
    none_type_0 = None
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = heap_0.insert(none_type_0)
    assert heap_0.heap_list == [0, None]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_1 = heap_1.build(list_0)
    assert heap_1.heap_list == [0, True, True, True, True]
    var_2 = heap_1.delete_min()
    assert var_2 is True
    assert heap_1.heap_list == [0, True, True, True]
    none_type_1 = None
    int_0 = -1489
    heap_2 = module_0.Heap()
    assert heap_2.heap_list == [0]
    var_3 = heap_2.percolate(int_0)
    var_4 = heap_0.min()

def test_case_9():
    bytes_0 = b'wI[\xfd\xc7\xdf\xb3L\xe2\xcf\xb8]\x0f3(\xa4\xd5w\x14'
    float_0 = 3124.94
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(bytes_0)
    assert heap_0.heap_list == [0, b'wI[\xfd\xc7\xdf\xb3L\xe2\xcf\xb8]\x0f3(\xa4\xd5w\x14']
    var_1 = heap_0.sift(float_0)

def test_case_10():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, False, False, False]
    var_1 = heap_0.insert(bool_0)
    assert heap_0.heap_list == [0, False, False, False, False]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_2 = heap_0.delete_min()
    assert var_2 is False
    assert heap_0.heap_list == [0, False, False, False]
