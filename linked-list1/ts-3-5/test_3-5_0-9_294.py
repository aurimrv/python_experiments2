import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

import pytest

# Test cases for ListNode class methods

def test_contains_cycle_single_node_no_cycle():
    node = ListNode(1)
    assert node.contains_cycle() is False

def test_contains_cycle_single_node_cycle():
    node = ListNode(1)
    node.next = node  # Point next to itself to create a cycle
    assert node.contains_cycle() is True

def test_get_beginning_of_cycle_if_exists_no_cycle():
    node = ListNode(1)
    assert node.get_beginning_of_cycle_if_exists() is None

def test_get_beginning_of_cycle_if_exists_cycle():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node2  # Create a cycle between node 2 and node 3
    assert node1.get_beginning_of_cycle_if_exists() == node2

def test_reverse_single_node():
    node = ListNode(5)
    new_head = node.reverse()
    assert new_head.val == 5
    assert new_head.next is None

def test_reverse_multiple_nodes():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    new_head = node1.reverse()

    assert new_head.val == 3
    assert new_head.next.val == 2
    assert new_head.next.next.val == 1

def test_reverse_recursive_single_node():
    node = ListNode(10)
    new_head = node.reverse_recursive()
    assert new_head.val == 10
    assert new_head.next is None

def test_reverse_recursive_multiple_nodes():
    node1 = ListNode(4)
    node2 = ListNode(7)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3

    new_head = node1.reverse_recursive()

    assert new_head.val == 2
    assert new_head.next.val == 7
    assert new_head.next.next.val == 4