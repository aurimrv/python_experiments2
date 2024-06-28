import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

# Test case for Trie class initialization
def test_trie_initialization():
    words = ['apple', 'banana', 'apricot']
    trie = Trie(words)
    assert trie is not None

# Test case for adding a word to the Trie
def test_trie_add_word():
    words = ['apple', 'banana', 'apricot']
    trie = Trie(words)
    word_to_add = 'cherry'
    trie.add(word_to_add)
    assert trie.get_all_common_prefix(word_to_add) == [word_to_add]

# Test case for getting common prefixes in the Trie
def test_trie_get_common_prefix():
    words = ['apple', 'banana', 'apricot']
    trie = Trie(words)
    
    common_prefix = 'ap'
    expected_words = ['apple', 'apricot']
    assert trie.get_all_common_prefix(common_prefix) == expected_words

    common_prefix = 'ba'
    expected_words = ['banana']
    assert trie.get_all_common_prefix(common_prefix) == expected_words

    common_prefix = 'c'
    expected_words = []
    assert trie.get_all_common_prefix(common_prefix) == expected_words