#Pyguin test cases converted from heap/MOSA/seed_1706/test_heap.py
import pytest
import heap as module_0

def test_case_0():
    bool_0 = False
    int_0 = -4832
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, -4832]

def test_case_1():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_0 = heap_1.min()

def test_case_2():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.min()
    var_1 = heap_0.size()
    assert var_1 == 0
    var_2 = heap_0.delete_min()
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]

def test_case_3():
    bytes_0 = b'}\x88A'
    bool_0 = False
    list_0 = [bytes_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, b'}\x88A']

def test_case_4():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]

def test_case_5():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    heap_1 = module_0.Heap()
    assert heap_1.heap_list == [0]
    var_0 = heap_0.size()
    assert var_0 == 0

def test_case_6():
    int_0 = -1604
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.size()
    assert var_0 == 0

def test_case_7():
    bool_0 = False
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(bool_0)
    assert heap_0.heap_list == [0, False]
    var_1 = heap_0.min()
    assert var_1 is False

def test_case_8():
    str_0 = "h2.{v2|'fg3i"
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(str_0)
    assert heap_0.heap_list == [0, "h2.{v2|'fg3i"]
    var_1 = heap_0.delete_min()
    assert var_1 == "h2.{v2|'fg3i"
    assert heap_0.heap_list == [0]

def test_case_9():
    int_0 = -4832
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(heap_0)

def test_case_10():
    int_0 = -397
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]

def test_case_11():
    bool_0 = False
    int_0 = -1604
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.find_min_child_index(bool_0)
    assert var_0 == 0
    var_1 = heap_0.min()

def test_case_12():
    none_type_0 = None
    int_0 = 1414
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.find_min_child_index(int_0)

def test_case_13():
    float_0 = 793.0
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.min()
    var_1 = heap_0.sift(float_0)

def test_case_14():
    bool_0 = False
    int_0 = -1604
    list_0 = [bool_0, int_0, bool_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, -1604, False, False]

def test_case_15():
    bool_0 = False
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.insert(bool_0)
    assert heap_0.heap_list == [0, False]
    var_1 = heap_0.min()
    assert var_1 is False
    var_2 = heap_0.find_min_child_index(var_1)
    assert var_2 == 1

def test_case_16():
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    bool_0 = True
    var_0 = heap_0.insert(bool_0)
    assert heap_0.heap_list == [0, True]
    int_0 = -3979
    var_1 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, -3979, True]

def test_case_17():
    bool_0 = False
    int_0 = -1604
    list_0 = [bool_0, int_0, bool_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, -1604, False, False]
    var_1 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, -1604, -1604, False, False]

def test_case_18():
    bool_0 = False
    int_0 = -1618
    list_0 = [int_0, bool_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, -1618, False]
    var_1 = heap_0.insert(int_0)
    assert heap_0.heap_list == [0, -1618, False, -1618]

def test_case_19():
    bool_0 = True
    int_0 = -1604
    none_type_0 = None
    list_0 = [bool_0, int_0, bool_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, -1604, True, True]
    var_1 = heap_0.delete_min()
    assert var_1 == -1604
    assert heap_0.heap_list == [0, True, True]

def test_case_20():
    int_0 = -1615
    bool_0 = False
    none_type_0 = None
    list_0 = [bool_0, int_0, none_type_0, bool_0, bool_0]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.delete_min()

def test_case_21():
    bool_0 = False
    int_0 = -1605
    bool_1 = False
    list_0 = [bool_0, int_0, bool_1, bool_1]
    heap_0 = module_0.Heap()
    assert heap_0.heap_list == [0]
    var_0 = heap_0.delete_min()
    var_1 = heap_0.build(list_0)
    assert heap_0.heap_list == [0, -1605, False, False, False]
