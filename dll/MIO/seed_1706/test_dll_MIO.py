#Pyguin test cases converted from dll/MIO/seed_1706/test_dll.py
import pytest
import dll as module_0

def test_case_0():
    bytes_0 = b'k\xf1\x9e'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'

def test_case_1():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList(double_linked_list_0)
    assert f'{type(double_linked_list_1).__module__}.{type(double_linked_list_1).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'dll.Node'

def test_case_2():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_3():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'

def test_case_4():
    bytes_0 = b"'T\t\xa4\xe0\x1dR4^\x86\xa4\xe3"
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_0 = double_linked_list_0.pop()
    assert var_0 == 227

def test_case_5():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'dll.DoubleLinkedList'
    assert var_1.head is None
    assert var_1.tail is None

def test_case_6():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.pop()

def test_case_7():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'

def test_case_8():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.append(var_0)

def test_case_9():
    str_0 = 'o]"X|\x0c?,M['
    double_linked_list_0 = module_0.DoubleLinkedList(str_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_0 = double_linked_list_0.shift()
    assert var_0 == 'o'

def test_case_10():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(var_1.head).__module__}.{type(var_1.head).__qualname__}' == 'dll.Node'
    assert var_1.tail is None

def test_case_11():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

def test_case_12():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.remove(double_linked_list_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_13():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(var_1.head).__module__}.{type(var_1.head).__qualname__}' == 'dll.Node'
    assert var_1.tail is None

def test_case_14():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.append(var_0)
    var_2 = double_linked_list_0.remove(var_0)

def test_case_15():
    none_type_0 = None
    bytes_0 = b'J\x94|\xbf'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(none_type_0)

def test_case_16():
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_17():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.append(var_0)
    var_2 = double_linked_list_0.push(var_0)
    var_3 = double_linked_list_0.remove(double_linked_list_0)

def test_case_18():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_19():
    node_0 = module_0.Node()

def test_case_20():
    node_0 = module_0.Node()
    var_0 = node_0.__repr__()
    assert var_0 == 'Value: None'
