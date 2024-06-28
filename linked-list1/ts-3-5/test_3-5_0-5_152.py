import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test when the list is empty
    node = ListNode(None)
    assert node.contains_cycle() == False

    # Test when the list has only one node
    node = ListNode(1)
    assert node.contains_cycle() == False

    # Test when the list has a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    assert node1.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test when the list is empty
    node = ListNode(None)
    assert node.get_beginning_of_cycle_if_exists() == None

    # Test when the list has only one node
    node = ListNode(1)
    assert node.get_beginning_of_cycle_if_exists() == None

    # Test when the list has a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    assert node1.get_beginning_of_cycle_if_exists() == node1

def test_reverse():
    # Test reversing a list with multiple nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    reversed_node = node1.reverse()
    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1

def test_reverse_recursive():
    # Test reversing a list with multiple nodes recursively
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    reversed_node = node1.reverse_recursive()
    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1