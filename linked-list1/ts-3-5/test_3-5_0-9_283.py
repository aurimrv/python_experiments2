import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

class TestListNode:

    # Test contains_cycle method
    def test_contains_cycle_no_cycle(self):
        node1 = ListNode(1)
        assert node1.contains_cycle() == False

    def test_contains_cycle_with_cycle(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node1
        assert node1.contains_cycle() == True

    # Test get_beginning_of_cycle_if_exists method
    def test_get_beginning_of_cycle_if_exists_no_cycle(self):
        node1 = ListNode(1)
        assert node1.get_beginning_of_cycle_if_exists() == None

    def test_get_beginning_of_cycle_if_exists_with_cycle(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node1
        assert node1.get_beginning_of_cycle_if_exists().val == 1

    # Test reverse method
    def test_reverse(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        new_head = node1.reverse()
        values = []
        while new_head:
            values.append(new_head.val)
            new_head = new_head.next
        assert values == [3, 2, 1]

    # Test reverse_recursive method
    def test_reverse_recursive(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        new_head = node1.reverse_recursive()
        values = []
        while new_head:
            values.append(new_head.val)
            new_head = new_head.next
        assert values == [3, 2, 1]