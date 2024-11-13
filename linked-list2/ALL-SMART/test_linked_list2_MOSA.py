#Pyguin test cases converted from linked-list2/MOSA/seed_1706/test_linked_list2.py
import pytest
import linked_list2 as module_0
import builtins as module_1

def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    linked_list_0 = module_0.LinkedList(list_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linked_list2.Node'
    none_type_0 = None
    var_0 = linked_list_0.search(none_type_0)

def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    linked_list_0 = module_0.LinkedList(list_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linked_list2.Node'
    var_0 = linked_list_0.size()
    assert var_0 == 2
    linked_list_1 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linked_list2.LinkedList'
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'linked_list2.Node'
    var_1 = linked_list_1.search(var_0)

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.size()
    assert var_0 == 0
    with pytest.raises(IndexError):
        linked_list_0.pop()

def test_case_4():
    int_0 = 1000
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.search(int_0)

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(linked_list_0)
    var_1 = linked_list_0.push(var_0)
    var_2 = linked_list_0.push(linked_list_0)
    bool_0 = True
    var_3 = linked_list_0.remove(linked_list_0)
    node_0 = module_0.Node(bool_0)
    var_4 = linked_list_0.push(var_3)

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(linked_list_0)
    var_1 = linked_list_0.push(var_0)
    var_2 = linked_list_0.push(linked_list_0)
    var_3 = linked_list_0.remove(var_0)
    none_type_0 = None
    var_4 = linked_list_0.remove(none_type_0)

def test_case_7():
    bytes_0 = b'\xbe'
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linked_list2.Node'
    var_0 = linked_list_0.search(linked_list_0)
    var_1 = linked_list_0.display()
    assert var_1 == '(190)'
    var_2 = linked_list_0.push(linked_list_0)
    var_3 = linked_list_0.remove(bytes_0)

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.display()
    assert var_0 == ')'

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    linked_list_2 = module_0.LinkedList()
    assert linked_list_2.head is None
    var_0 = linked_list_2.size()
    assert var_0 == 0

def test_case_10():
    object_0 = module_1.object()
    bool_0 = False
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    bytes_0 = b'\xea\xa9OG\xab\xc9y\x9d\xd7\x9f\x95]!\xb1\x03\x1d5"\xd5'
    linked_list_1 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'linked_list2.Node'
    var_0 = linked_list_1.pop()
    assert var_0 == 213
    var_1 = linked_list_0.push(var_0)
    bool_1 = True
    var_2 = linked_list_1.remove(bool_1)
    node_0 = module_0.Node(var_2)

def test_case_11():
    bytes_0 = b'\x84\xa9)\xc1\x81\xbb!\xb3\xf4\x8b\xa7\xde.\xef'
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linked_list2.Node'
    var_0 = linked_list_0.search(linked_list_0)
    var_1 = linked_list_0.display()
    assert var_1 == '(239, 46, 222, 167, 139, 244, 179, 33, 187, 129, 193, 41, 169, 132)'
    var_2 = linked_list_0.push(linked_list_0)

def test_case_12():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linked_list2.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.search(linked_list_0)
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'linked_list2.Node'
    var_1 = linked_list_0.display()
    assert var_1 == ')'
    var_2 = linked_list_1.search(linked_list_0)
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linked_list2.Node'
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linked_list2.LinkedList'
    assert var_2.next is None
