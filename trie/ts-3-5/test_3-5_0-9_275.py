import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

# Test cases for the Trie class

def test_trie_init_one_word():
    words = ['apple']
    trie = Trie(words)
    assert trie.get_all_common_prefix('a') == ['apple']

def test_trie_init_multiple_words():
    words = ['apple', 'banana', 'orange']
    trie = Trie(words)
    assert trie.get_all_common_prefix('a') == ['apple']
    assert trie.get_all_common_prefix('b') == ['banana']
    assert trie.get_all_common_prefix('o') == ['orange']

def test_trie_add_word():
    words = ['apple']
    trie = Trie(words)
    trie.add('banana')
    assert trie.get_all_common_prefix('b') == ['banana']

def test_trie_get_all_common_prefix():
    words = ['apple', 'banana', 'orange']
    trie = Trie(words)
    assert trie.get_all_common_prefix('app') == ['apple']
    assert trie.get_all_common_prefix('ban') == ['banana']
    assert trie.get_all_common_prefix('or') == ['orange']

def test_trie_get_all_common_prefix_no_prefix_match():
    words = ['apple', 'banana', 'orange']
    trie = Trie(words)
    assert trie.get_all_common_prefix('xyz') == []
