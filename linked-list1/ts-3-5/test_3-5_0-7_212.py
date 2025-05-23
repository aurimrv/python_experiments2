import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list1 import ListNode

def test_contains_cycle():
    # Test with a single node without a cycle
    node1 = ListNode(1)
    assert node1.contains_cycle() == False

    # Test with a cycle
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert node2.contains_cycle() == True

def test_get_beginning_of_cycle_if_exists():
    # Test with a single node without a cycle
    node1 = ListNode(1)
    assert node1.get_beginning_of_cycle_if_exists() == None

    # Test with a cycle
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert node2.get_beginning_of_cycle_if_exists() == node2

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
    # Test recursive reverse with a list of nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    reversed_node = node1.reverse_recursive()
    assert reversed_node.val == 3
    assert reversed_node.next.val == 2
    assert reversed_node.next.next.val == 1