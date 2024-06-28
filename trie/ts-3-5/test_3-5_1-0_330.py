import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

# Test Cases for Trie class

@pytest.fixture
def test_trie():
    words = ['apple', 'banana', 'application', 'ape']
    return Trie(words)

def test_trie_initialization(test_trie):
    assert 'a' in test_trie.head
    assert 'b' in test_trie.head
    assert 'e' not in test_trie.head

def test_trie_add_word(test_trie):
    test_trie.add('test')
    assert 't' in test_trie.head
    assert 'e' in test_trie.head['t']
    assert 's' in test_trie.head['t']['e']

def test_trie_get_all_common_prefix(test_trie):
    assert test_trie.get_all_common_prefix('app') == ['apple', 'application']

def test_trie_get_all_common_prefix_empty(test_trie):
    assert test_trie.get_all_common_prefix('xyz') == []

def test_trie_get_all_common_prefix_partial(test_trie):
    assert test_trie.get_all_common_prefix('ap') == ['apple', 'application', 'ape']