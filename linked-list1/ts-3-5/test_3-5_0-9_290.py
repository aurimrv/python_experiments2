import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case: Empty list should not contain a cycle
    node = ListNode(1)
    assert node.contains_cycle() == False

    # Test case: Single node list should not contain a cycle
    node.next = ListNode(2)
    assert node.contains_cycle() == False

    # Test case: List with cycle should return True
    node.next.next = node
    assert node.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test case: Empty list should not contain a cycle
    node = ListNode(1)
    assert node.get_beginning_of_cycle_if_exists() == None

    # Test case: Single node list should not contain a cycle
    node.next = ListNode(2)
    assert node.get_beginning_of_cycle_if_exists() == None

    # Test case: List with cycle should return the start of the cycle
    node.next.next = node
    assert node.get_beginning_of_cycle_if_exists() == node

def test_reverse():
    # Test case: Reverse a list of one node
    node = ListNode(1)
    reversed_node = node.reverse()
    assert reversed_node.val == 1
    assert reversed_node.next == None

    # Test case: Reverse a list of multiple nodes
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    reversed_node = node.reverse()
    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1

def test_reverse_recursive():
    # Test case: Reverse recursively a list of one node
    node = ListNode(1)
    reversed_node = node.reverse_recursive()
    assert reversed_node.val == 1
    assert reversed_node.next == None

    # Test case: Reverse recursively a list of multiple nodes
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    reversed_node = node.reverse_recursive()
    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1