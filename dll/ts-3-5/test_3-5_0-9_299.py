import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from dll import Node, DoubleLinkedList

import pytest

class TestDoubleLinkedList:

    @pytest.fixture
    def setup_dll(self):
        dll = DoubleLinkedList()
        dll.push(1)
        dll.push(2)
        dll.push(3)
        return dll

    def test_push(self, setup_dll):
        assert setup_dll.head.data == 3
        assert setup_dll.tail.data == 1

    def test_pop(self, setup_dll):
        assert setup_dll.pop() == 3
        assert setup_dll.head.data == 2

    def test_append(self, setup_dll):
        setup_dll.append(4)
        assert setup_dll.tail.data == 4

    def test_shift(self, setup_dll):
        assert setup_dll.shift() == 1
        assert setup_dll.tail.data == 2

    def test_remove(self, setup_dll):
        setup_dll.remove(2)
        assert setup_dll.head.data == 3

    def test_empty_list_error_on_pop(self):
        dll = DoubleLinkedList()
        with pytest.raises(IndexError):
            dll.pop()

    def test_empty_list_error_on_shift(self):
        dll = DoubleLinkedList()
        with pytest.raises(IndexError):
            dll.shift()

    def test_remove_non_existing_element(self, setup_dll):
        with pytest.raises(ValueError):
            setup_dll.remove(4)

    def test_list_representation(self):
        dll = DoubleLinkedList([1, 2, 3])
        assert dll._repr() == [3, 2, 1]