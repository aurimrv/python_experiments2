import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    words = ['apple', 'app', 'application', 'applause']
    assert find_longest_common_prefix(words) == 'app'

    words = ['flower', 'fly', 'flour', 'flame']
    assert find_longest_common_prefix(words) == 'fl'

def test_find_longest_common_prefix_reduce():
    words = ['apple', 'app', 'application', 'applause']
    assert find_longest_common_prefix_reduce(words) == 'app'

    words = ['flower', 'fly', 'flour', 'flame']
    assert find_longest_common_prefix_reduce(words) == 'fl'