import os
import sys
from functools import reduce
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    words1 = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix(words1) == 'fl'

    words2 = ['dog', 'race', 'car']
    assert find_longest_common_prefix(words2) == ''

def test_find_longest_common_prefix_reduce():
    words1 = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix_reduce(words1) == 'fl'

    words2 = ['dog', 'race', 'car']
    assert find_longest_common_prefix_reduce(words2) == ''