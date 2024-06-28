import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test case 1: Single node, no cycle
    node1 = ListNode(1)
    assert node1.contains_cycle() == False
    
    # Test case 2: Cycle present
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3  # Cycle
    
    assert node2.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test case 1: Single node, no cycle
    node1 = ListNode(1)
    assert node1.get_beginning_of_cycle_if_exists() == None
    
    # Test case 2: Cycle present
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3  # Cycle
    
    assert node2.get_beginning_of_cycle_if_exists().val == 3

def test_reverse():
    # Test case 1: Single node
    node1 = ListNode(1)
    reversed_node1 = node1.reverse()
    assert reversed_node1.val == 1 and reversed_node1.next == None
    
    # Test case 2: Multiple nodes
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node2.next = node3
    node3.next = node4
    
    reversed_node2 = node2.reverse()
    assert reversed_node2.val == 4 and reversed_node2.next.val == 3 and reversed_node2.next.next.val == 2

def test_reverse_recursive():
    # Test case 1: Single node
    node1 = ListNode(1)
    reversed_node1 = node1.reverse_recursive()
    assert reversed_node1.val == 1 and reversed_node1.next == None
    
    # Test case 2: Multiple nodes
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node2.next = node3
    node3.next = node4
    
    reversed_node2 = node2.reverse_recursive()
    assert reversed_node2.val == 4 and reversed_node2.next.val == 3 and reversed_node2.next.next.val == 2