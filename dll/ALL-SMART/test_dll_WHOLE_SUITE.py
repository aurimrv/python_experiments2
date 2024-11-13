#Pyguin test cases converted from dll/WHOLE_SUITE/seed_1706/test_dll.py
import pytest
import dll as module_0
import builtins as module_1

def test_case_0():
    none_type_0 = None
    node_0 = module_0.Node(prev=none_type_0)
    var_0 = node_0.__repr__()
    assert var_0 == 'Value: None'

def test_case_1():
    bytes_0 = b'qk\xbdA\xf4\xdd\x05D\xdd\xca\x13\x87\xbe\xd8=-\x9dF'
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(bytes_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.shift()
    assert var_1 == b'qk\xbdA\xf4\xdd\x05D\xdd\xca\x13\x87\xbe\xd8=-\x9dF'
    assert double_linked_list_0.tail is None

def test_case_2():
    object_0 = module_1.object()
    str_0 = "4'L`\x0bAeH"
    str_1 = 'TB@nM.Y\tPr^e:f@n8'
    double_linked_list_0 = module_0.DoubleLinkedList(str_1)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_0 = double_linked_list_0.shift()
    assert var_0 == 'T'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(str_0)

def test_case_3():
    none_type_0 = None
    double_linked_list_0 = module_0.DoubleLinkedList(none_type_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.pop()

def test_case_4():
    bytes_0 = b'<'
    node_0 = module_0.Node(bytes_0)
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(bytes_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    double_linked_list_1 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_1).__module__}.{type(double_linked_list_1).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.push(double_linked_list_0)
    var_2 = double_linked_list_1.push(node_0)
    var_3 = double_linked_list_0.append(double_linked_list_0)
    var_4 = var_3.__repr__()
    var_5 = var_4.__repr__()
    var_6 = double_linked_list_0.pop()
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(var_6.head).__module__}.{type(var_6.head).__qualname__}' == 'dll.Node'
    assert f'{type(var_6.tail).__module__}.{type(var_6.tail).__qualname__}' == 'dll.Node'
    var_7 = double_linked_list_0.shift()
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(var_7.head).__module__}.{type(var_7.head).__qualname__}' == 'dll.Node'
    assert f'{type(var_7.tail).__module__}.{type(var_7.tail).__qualname__}' == 'dll.Node'
    var_8 = double_linked_list_0.shift()
    assert var_8 == b'<'
    assert double_linked_list_0.tail is None
    assert var_6.tail is None
    assert var_7.tail is None
    double_linked_list_2 = module_0.DoubleLinkedList()
    assert double_linked_list_2.head is None
    assert double_linked_list_2.tail is None
    with pytest.raises(ValueError):
        double_linked_list_2.remove(double_linked_list_0)

def test_case_5():
    str_0 = 'fYzrco`K}IYz^;u.A'
    int_0 = -217
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(str_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    str_1 = "%9\x0b'w)=W\rFi'W3OxN#"
    var_1 = double_linked_list_0.append(str_1)
    var_2 = var_1.__repr__()
    var_3 = double_linked_list_0.pop()
    assert var_3 == 'fYzrco`K}IYz^;u.A'

def test_case_6():
    str_0 = 'moNk'
    double_linked_list_0 = module_0.DoubleLinkedList(str_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_1).__module__}.{type(double_linked_list_1).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    bool_0 = True
    node_0 = module_0.Node(bool_0)
    with pytest.raises(IndexError):
        double_linked_list_1.shift()

def test_case_7():
    float_0 = -674.0
    none_type_0 = None
    node_0 = module_0.Node(float_0, none_type_0)
    double_linked_list_0 = module_0.DoubleLinkedList(float_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    double_linked_list_1 = module_0.DoubleLinkedList(none_type_0)
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    var_0 = double_linked_list_1.push(double_linked_list_1)
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_1.push(none_type_0)
    var_2 = double_linked_list_0.remove(float_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    str_0 = '\\8\t!XBv4'
    var_3 = var_2.__repr__()
    node_1 = module_0.Node(str_0, float_0)
    int_0 = -1335
    object_0 = module_1.object()
    int_1 = -2803
    double_linked_list_2 = module_0.DoubleLinkedList()
    var_4 = double_linked_list_2.append(int_1)
    assert f'{type(double_linked_list_2.head).__module__}.{type(double_linked_list_2.head).__qualname__}' == 'dll.Node'
    var_5 = var_4.__repr__()

def test_case_8():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    set_0 = {double_linked_list_0, double_linked_list_0, double_linked_list_0, double_linked_list_0}
    var_0 = double_linked_list_0.push(set_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.append(double_linked_list_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)
    var_3 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_9():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    set_0 = {double_linked_list_0, double_linked_list_0, double_linked_list_0, double_linked_list_0}
    var_0 = double_linked_list_0.push(set_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'dll.Node'
    var_1 = double_linked_list_0.append(double_linked_list_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)
    var_3 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_10():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'dll.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'dll.Node'
    set_0 = {double_linked_list_0, double_linked_list_0, double_linked_list_0, double_linked_list_0}
    var_1 = double_linked_list_0.push(set_0)
    var_2 = double_linked_list_0.append(double_linked_list_0)
    var_3 = double_linked_list_0.remove(double_linked_list_0)
    var_4 = double_linked_list_0.pop()
