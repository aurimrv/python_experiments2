import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

class TestListNode:

    def test_contains_cycle(self):
        # Create a linked list with no cycle
        n1 = ListNode(1)
        assert n1.contains_cycle() == False

        # Create a linked list with a cycle
        n2 = ListNode(1)
        n2.next = n2  # Create a cycle
        assert n2.contains_cycle() == True

    def test_get_beginning_of_cycle_if_exists(self):
        # Test when there is no cycle
        n1 = ListNode(1)
        assert n1.get_beginning_of_cycle_if_exists() == None

        # Test when there is a cycle
        n2 = ListNode(1)
        n3 = ListNode(2)
        n4 = ListNode(3)
        n2.next = n3
        n3.next = n4
        n4.next = n3  # Create a cycle
        assert n2.get_beginning_of_cycle_if_exists() == n3

    def test_reverse(self):
        # Test reversing a simple linked list
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n1.next = n2
        n2.next = n3
        reversed_list = n1.reverse()
        assert reversed_list.val == 3
        assert reversed_list.next.val == 2
        assert reversed_list.next.next.val == 1

    def test_reverse_recursive(self):
        # Test reversing a simple linked list using recursion
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n1.next = n2
        n2.next = n3
        reversed_list = n1.reverse_recursive()
        assert reversed_list.val == 3
        assert reversed_list.next.val == 2
        assert reversed_list.next.next.val == 1