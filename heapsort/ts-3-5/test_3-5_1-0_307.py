import sys
import os
from copy import deepcopy
from heapq import heapify, heappop

# Append project directory to the system path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import heapsort

def test_heap_sort():
    assert heapsort.heap_sort([]) == []
    input_list = [4, 2, 7, 1, 5]
    expected_output = [1, 2, 4, 5, 7]
    assert heapsort.heap_sort(input_list) == expected_output
    input_list = [-3, -1, -5, -2, -4]
    expected_output = [-5, -4, -3, -2, -1]
    assert heapsort.heap_sort(input_list) == expected_output

def test_max_heap_sort():
    assert heapsort.max_heap_sort([]) == []
    input_list = [4, 2, 7, 1, 5]
    expected_output = [7, 5, 4, 2, 1]
    assert heapsort.max_heap_sort(input_list) == expected_output
    input_list = [-3, -1, -5, -2, -4]
    expected_output = [-1, -2, -3, -4, -5]
    assert heapsort.max_heap_sort(input_list) == expected_output

def test_custom_heap_sort():
    assert heapsort.custom_heap_sort([], sort='min') == []
    input_list = [4, 2, 7, 1, 5]
    expected_output = [1, 2, 4, 5, 7]
    assert heapsort.custom_heap_sort(input_list, sort='min') == expected_output
    input_list = [4, 2, 7, 1, 5]
    expected_output = [7, 5, 4, 2, 1]
    assert heapsort.custom_heap_sort(input_list, sort='max') == expected_output
    input_list = [-3, -1, -5, -2, -4]
    expected_output = [-5, -4, -3, -2, -1]
    assert heapsort.custom_heap_sort(input_list, sort='min') == expected_output
    input_list = [-3, -1, -5, -2, -4]
    expected_output = [-1, -2, -3, -4, -5]
    assert heapsort.custom_heap_sort(input_list, sort='max') == expected_output