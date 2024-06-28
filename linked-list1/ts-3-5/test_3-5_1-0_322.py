import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

import pytest

class TestListNode:
    
    def test_contains_cycle_no_cycle(self):
        # Test when there is no cycle in the linked list
        node_1 = ListNode(1)
        assert node_1.contains_cycle() == False
    
    def test_contains_cycle_with_cycle(self):
        # Test when there is a cycle in the linked list
        node_1 = ListNode(1)
        node_2 = ListNode(2)
        node_3 = ListNode(3)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_1  # creating a cycle
        assert node_1.contains_cycle() == True

    def test_get_beginning_of_cycle_if_exists_no_cycle(self):
        # Test when there is no cycle in the linked list
        node_1 = ListNode(1)
        assert node_1.get_beginning_of_cycle_if_exists() == None
    
    def test_get_beginning_of_cycle_if_exists_with_cycle(self):
        # Test when there is a cycle in the linked list
        node_1 = ListNode(1)
        node_2 = ListNode(2)
        node_3 = ListNode(3)
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = node_1  # creating a cycle
        assert node_1.get_beginning_of_cycle_if_exists().val == 1
    
    def test_reverse(self):
        # Test reversing a simple linked list
        node_1 = ListNode(1)
        node_2 = ListNode(2)
        node_3 = ListNode(3)
        node_1.next = node_2
        node_2.next = node_3
        
        reversed_head = node_1.reverse()
        assert reversed_head.val == 3
        assert reversed_head.next.val == 2
        assert reversed_head.next.next.val == 1
    
    def test_reverse_recursive(self):
        # Test reversing a simple linked list using recursion
        node_1 = ListNode(1)
        node_2 = ListNode(2)
        node_3 = ListNode(3)
        node_1.next = node_2
        node_2.next = node_3
        
        reversed_head = node_1.reverse_recursive()
        assert reversed_head.val == 3
        assert reversed_head.next.val == 2
        assert reversed_head.next.next.val == 1