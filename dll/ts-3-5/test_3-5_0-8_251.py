import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

@pytest.fixture
def setup_dll():
    dll = DoubleLinkedList()
    return dll

def test_node_creation():
    node = Node(5)
    assert node.data == 5

def test_push_method(setup_dll):
    setup_dll.push(1)
    assert setup_dll.head.data == 1
    assert setup_dll.tail.data == 1

    setup_dll.push(2)
    assert setup_dll.head.data == 2
    assert setup_dll.tail.data == 1

def test_pop_method(setup_dll):
    setup_dll.push(1)
    setup_dll.push(2)

    assert setup_dll.pop() == 2
    assert setup_dll.head.data == 1

def test_append_method(setup_dll):
    setup_dll.append(1)
    assert setup_dll.tail.data == 1
    assert setup_dll.head.data == 1

    setup_dll.append(2)
    assert setup_dll.tail.data == 2
    assert setup_dll.head.data == 1

def test_shift_method(setup_dll):
    setup_dll.push(1)
    setup_dll.push(2)

    assert setup_dll.shift() == 1
    assert setup_dll.tail.data == 2

def test_remove_method(setup_dll):
    setup_dll.push(1)
    setup_dll.push(2)
    setup_dll.push(3)

    setup_dll.remove(2)
    assert setup_dll.head.data == 3
    assert setup_dll.tail.data == 1

def test_remove_method_not_present(setup_dll):
    setup_dll.push(1)
    setup_dll.push(2)

    with pytest.raises(ValueError):
        setup_dll.remove(3)