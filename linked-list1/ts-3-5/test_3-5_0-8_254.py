import os
import sys
import pytest

# Add project directory to import modules correctly
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test when the list is empty
    assert ListNode(None).contains_cycle() == False
    
    # Test when the list has only one node without a cycle
    node1 = ListNode(1)
    assert node1.contains_cycle() == False
    
    # Test when the list has a cycle
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert node2.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test when the list is empty
    assert ListNode(None).get_beginning_of_cycle_if_exists() == None
    
    # Test when the list has only one node without a cycle
    node1 = ListNode(1)
    assert node1.get_beginning_of_cycle_if_exists() == None
    
    # Test when the list has a cycle
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert node2.get_beginning_of_cycle_if_exists().val == 2

def test_reverse():
    # Test reverse on a list with multiple nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_head = node1.reverse()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1

def test_reverse_recursive():
    # Test reverse_recursive on a list with multiple nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_head = node1.reverse_recursive()
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1