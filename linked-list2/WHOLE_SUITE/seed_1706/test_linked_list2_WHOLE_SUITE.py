#Pyguin test cases converted from linked-list2/WHOLE_SUITE/seed_1706/test_linked_list2.py
import pytest
import linked_list2 as module_0

def test_case_0():
    bool_0 = False
    linked_list_0 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.push(bool_0)
    none_type_0 = None
    var_2 = linked_list_0.push(none_type_0)
    var_3 = linked_list_0.display()
    var_4 = linked_list_0.display()
    var_5 = linked_list_0.pop()
    var_6 = linked_list_0.remove(linked_list_0)

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None

def test_case_2():
    int_0 = 2850
    list_0 = [int_0, int_0, int_0, int_0]
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.display()
    assert var_0 == ')'
    var_1 = linked_list_0.remove(list_0)

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.size()
    assert var_0 == 0

def test_case_4():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.display()
    assert var_0 == ')'

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'linked_list2.Node'
    var_0 = linked_list_1.remove(linked_list_0)
    assert linked_list_1.head is None
    linked_list_2 = module_0.LinkedList()
    assert linked_list_2.head is None
    var_1 = linked_list_2.push(linked_list_0)

def test_case_6():
    none_type_0 = None
    bool_0 = True
    list_0 = [bool_0]
    none_type_1 = None
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.search(none_type_0)
    node_0 = module_0.Node(none_type_1)
    var_1 = linked_list_0.push(list_0)

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    with pytest.raises(IndexError):
        linked_list_1.pop()

def test_case_8():
    bytes_0 = b'\xc7\x9d\xec\xa14\xc8\xf4\xbb\xe7J\xd6\xf3'
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linked_list2.Node'
    var_0 = linked_list_0.pop()
    assert var_0 == 243
    var_1 = linked_list_0.remove(bytes_0)
    var_2 = linked_list_0.search(bytes_0)
    var_3 = linked_list_0.remove(var_0)
    node_0 = module_0.Node(var_3)

def test_case_9():
    bool_0 = True
    node_0 = module_0.Node(bool_0, bool_0)
    linked_list_0 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linked_list2.Node'
    var_0 = linked_list_0.search(bool_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linked_list2.Node'
    assert var_0.data is True
    assert var_0.next is None

def test_case_10():
    bytes_0 = b'\xe3\xd9\x98\x08\xd7\xbb=\x02\x08'
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linked_list2.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(8, 2, 61, 187, 215, 8, 152, 217, 227)'

def test_case_11():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    with pytest.raises(IndexError):
        linked_list_0.pop()
