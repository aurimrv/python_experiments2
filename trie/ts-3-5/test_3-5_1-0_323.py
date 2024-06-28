import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

def test_trie_initialization():
    words = ['apple', 'banana', 'cat']
    trie = Trie(words)
    assert len(trie.head) == 3
    
def test_trie_add():
    words = ['apple', 'banana', 'cat']
    trie = Trie(words)
    trie.add('dog')
    assert 'd' in trie.head
    assert 'o' in trie.head['d']
    assert 'g' in trie.head['d']['o']
    assert trie.head['d']['o']['g'] == {'__eof__': '__eof__'}
    
def test_get_all_common_prefix_existing():
    words = ['apple', 'banana', 'cat']
    trie = Trie(words)
    common_prefix = trie.get_all_common_prefix('app')
    assert 'apple' in common_prefix
    assert len(common_prefix) == 1

def test_get_all_common_prefix_nonexistent():
    words = ['apple', 'banana', 'cat']
    trie = Trie(words)
    common_prefix = trie.get_all_common_prefix('zeb')
    assert common_prefix == []

def test_get_all_common_prefix_partial_existence():
    words = ['apple', 'banana', 'cat']
    trie = Trie(words)
    common_prefix = trie.get_all_common_prefix('ba')
    assert 'banana' in common_prefix
    assert len(common_prefix) == 1