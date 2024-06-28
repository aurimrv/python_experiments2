import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__));
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from linked_list1 import ListNode

import pytest

# Test cases for ListNode class methods

def test_contains_cycle_empty_list():
    # Test if an empty list does not contain a cycle
    node = ListNode(1)
    assert node.contains_cycle() == False

def test_contains_cycle_single_node_list():
    # Test if a single node list does not contain a cycle
    node = ListNode(1)
    node.next = None
    assert node.contains_cycle() == False

def test_get_beginning_of_cycle_if_exists_no_cycle():
    # Test if no cycle exists in the list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert node1.get_beginning_of_cycle_if_exists() == None

def test_reverse_single_node_list():
    # Test reversing a single node list
    node = ListNode(1)
    node_reversed = node.reverse()
    assert node_reversed.val == 1
    assert node_reversed.next == None

def test_reverse_recursive_multiple_nodes():
    # Test reversing a list using the recursive method
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    reversed_head = node1.reverse_recursive()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1
    assert reversed_head.next.next.next == None

def test_reverse_multiple_nodes():
    # Test reversing a list using the iterative method
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    
    reversed_head = node1.reverse()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1
    assert reversed_head.next.next.next == None
