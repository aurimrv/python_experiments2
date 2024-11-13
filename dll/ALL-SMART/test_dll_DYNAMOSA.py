#Pyguin test cases converted from dll/DYNAMOSA/seed_1706/test_dll.py
import pytest
import dll as module_0
import builtins as module_1

def test_case_0():
    float_0 = 739.5
    int_0 = -1616
    bool_0 = True
    tuple_0 = (int_0, bool_0, bool_0)
    set_0 = {tuple_0, tuple_0}
    double_linked_list_0 = module_0.DoubleLinkedList(set_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_0 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_1():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_2():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    none_type_0 = None
    var_0 = double_linked_list_0.push(none_type_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    none_type_1 = None
    var_1 = double_linked_list_0.push(none_type_1)
    var_2 = double_linked_list_0.remove(none_type_1)
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    var_3 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_3():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    none_type_0 = None
    var_0 = double_linked_list_0.push(none_type_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.remove(none_type_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.pop()

def test_case_4():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    str_0 = 'iB]J,<H\x0c[W2@NJ(~'
    var_1 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'dll.DoubleLinkedList'
    assert var_1.head is None
    assert var_1.tail is None
    var_2 = var_1.push(var_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    assert f'{type(var_1.head).__module__}.{type(var_1.head).__qualname__}' == 'dll.Node'
    assert f'{type(var_1.tail).__module__}.{type(var_1.tail).__qualname__}' == 'dll.Node'
    var_3 = double_linked_list_0.append(str_0)
    var_4 = var_1.remove(str_0)

def test_case_5():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.append(var_0)
    var_2 = double_linked_list_0.remove(var_0)

def test_case_6():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

def test_case_7():
    bytes_0 = b'\x83zi<e+\xc0)y\xe9\xdb\x01\xdf\x17\xdb'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_0 = double_linked_list_0.shift()
    assert var_0 == 131

def test_case_8():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    none_type_0 = None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(none_type_0)

def test_case_9():
    node_0 = module_0.Node()

def test_case_10():
    node_0 = module_0.Node()
    var_0 = node_0.__repr__()
    assert var_0 == 'Value: None'

def test_case_11():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    double_linked_list_1 = module_0.DoubleLinkedList(double_linked_list_0)
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.remove(double_linked_list_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    node_0 = module_0.Node(var_1, prev=double_linked_list_1)
    double_linked_list_2 = module_0.DoubleLinkedList()
    assert double_linked_list_2.head is None
    assert double_linked_list_2.tail is None
    var_2 = node_0.__repr__()
    assert var_2 == 'Value: None'
    var_3 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_4 = var_0.__repr__()

def test_case_12():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(var_1.head).__module__}.{type(var_1.head).__qualname__}' == 'dll.Node'
    assert var_1.tail is None

def test_case_13():
    bool_0 = False
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    double_linked_list_2 = module_0.DoubleLinkedList()
    assert double_linked_list_2.head is None
    assert double_linked_list_2.tail is None
    var_0 = double_linked_list_1.append(double_linked_list_1)
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_2.push(double_linked_list_1)
    assert f'{type(double_linked_list_2.tail).__module__}.{type(double_linked_list_2.tail).__qualname__}' == 'dll.Node'
    with pytest.raises(ValueError):
        double_linked_list_2.remove(bool_0)

def test_case_14():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.append(double_linked_list_0)
    str_0 = 'iB]J,<H@[W2@NJ(~'
    none_type_0 = None
    var_2 = double_linked_list_0.pop()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(var_2.head).__module__}.{type(var_2.head).__qualname__}' == 'dll.Node'
    assert f'{type(var_2.tail).__module__}.{type(var_2.tail).__qualname__}' == 'dll.Node'
    var_3 = var_2.push(none_type_0)
    var_4 = double_linked_list_0.append(str_0)
    var_5 = var_2.remove(str_0)

def test_case_15():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    none_type_0 = None
    var_0 = double_linked_list_0.append(none_type_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    var_1 = var_0.__repr__()
    var_2 = double_linked_list_0.push(double_linked_list_0)
    str_0 = 'iB]J,<H\x0c[W2@NJ(~'
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    none_type_1 = None
    var_3 = double_linked_list_0.pop()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(var_3.head).__module__}.{type(var_3.head).__qualname__}' == 'dll.Node'
    assert f'{type(var_3.tail).__module__}.{type(var_3.tail).__qualname__}' == 'dll.Node'
    var_4 = var_3.append(str_0)
    object_0 = module_1.object()
    var_5 = double_linked_list_0.append(str_0)
    var_6 = var_3.remove(str_0)
    var_7 = double_linked_list_1.push(str_0)
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'dll.Node'
    double_linked_list_2 = module_0.DoubleLinkedList(none_type_1)
    assert double_linked_list_2.head is None
    assert double_linked_list_2.tail is None
    with pytest.raises(IndexError):
        double_linked_list_2.pop()
