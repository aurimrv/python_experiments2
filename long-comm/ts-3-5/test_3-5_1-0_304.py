import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty_words():
    assert find_longest_common_prefix([]) == ''

def test_find_longest_common_prefix_single_word():
    assert find_longest_common_prefix(['apple']) == 'apple'

def test_find_longest_common_prefix_same_words():
    assert find_longest_common_prefix(['hello', 'hello', 'hello']) == 'hello'

def test_find_longest_common_prefix_no_common_prefix():
    assert find_longest_common_prefix(['apple', 'banana', 'carrot']) == ''

def test_find_longest_common_prefix_complex_case():
    assert find_longest_common_prefix(['alphabet', 'alpine', 'ape', 'ability']) == 'a'

def test_find_longest_common_prefix_reduce_empty_words():
    assert find_longest_common_prefix_reduce([]) == ''

def test_find_longest_common_prefix_reduce_single_word():
    assert find_longest_common_prefix_reduce(['apple']) == 'apple'

def test_find_longest_common_prefix_reduce_same_words():
    assert find_longest_common_prefix_reduce(['hello', 'hello', 'hello']) == 'hello'

def test_find_longest_common_prefix_reduce_no_common_prefix():
    assert find_longest_common_prefix_reduce(['apple', 'banana', 'carrot']) == ''

def test_find_longest_common_prefix_reduce_complex_case():
    assert find_longest_common_prefix_reduce(['alphabet', 'alpine', 'ape', 'ability']) == 'a'