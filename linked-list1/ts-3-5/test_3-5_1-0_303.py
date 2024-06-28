import os
import sys

# Add the project directory to the sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

import pytest

class TestListNode:

    def test_contains_cycle_empty_list(self):
        node = ListNode(1)
        assert node.contains_cycle() == False

    def test_contains_cycle_single_node_without_cycle(self):
        node = ListNode(1)
        node.next = ListNode(2)
        assert node.contains_cycle() == False

    def test_contains_cycle_cycle_exists(self):
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = node
        assert node.contains_cycle() == True
        
    def test_get_beginning_of_cycle_if_exists_empty_list(self):
        node = ListNode(1)
        assert node.get_beginning_of_cycle_if_exists() == None

    def test_get_beginning_of_cycle_if_exists_single_node_without_cycle(self):
        node = ListNode(1)
        node.next = ListNode(2)
        assert node.get_beginning_of_cycle_if_exists() == None

    def test_get_beginning_of_cycle_if_exists_cycle_exists(self):
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = node
        assert node.get_beginning_of_cycle_if_exists() == node

    def test_reverse_empty_list(self):
        node = ListNode(1)
        reversed_node = node.reverse()
        assert reversed_node.val == 1
        assert reversed_node.next == None

    def test_reverse_multiple_nodes(self):
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        reversed_node = node.reverse()
        assert reversed_node.val == 3
        assert reversed_node.next.val == 2
        assert reversed_node.next.next.val == 1
        assert reversed_node.next.next.next == None

    def test_reverse_recursive_empty_list(self):
        node = ListNode(1)
        reversed_node = node.reverse_recursive()
        assert reversed_node.val == 1
        assert reversed_node.next == None

    def test_reverse_recursive_multiple_nodes(self):
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        reversed_node = node.reverse_recursive()
        assert reversed_node.val == 3
        assert reversed_node.next.val == 2
        assert reversed_node.next.next.val == 1
        assert reversed_node.next.next.next == None