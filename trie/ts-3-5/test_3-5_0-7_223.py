import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

def test_trie_init():
    words = ['apple', 'banana', 'cherry']
    trie = Trie(words)
    assert trie.head == {'a': {'p': {'p': {'l': {'e': {'__eof__': '__eof__'}}}}}, 'b': {'a': {'n': {'a': {'n': {'a': {'__eof__': '__eof__'}}}}}}, 'c': {'h': {'e': {'r': {'r': {'y': {'__eof__': '__eof__'}}}}}}}

def test_trie_add():
    trie = Trie([])
    trie.add('dog')
    assert trie.head == {'d': {'o': {'g': {'__eof__': '__eof__'}}}}

def test_trie_get_all_common_prefix():
    words = ['apple', 'banana', 'cherry']
    trie = Trie(words)
    common_prefix = trie.get_all_common_prefix('b')
    assert common_prefix == ['banana']

def test_trie_get_all_common_prefix_multiple():
    words = ['apple', 'banana', 'cherry']
    trie = Trie(words)
    common_prefix = trie.get_all_common_prefix('c')
    assert common_prefix == ['cherry']

def test_trie_get_all_common_prefix_no_match():
    words = ['apple', 'banana', 'cherry']
    trie = Trie(words)
    common_prefix = trie.get_all_common_prefix('x')
    assert common_prefix == []

def test_trie_get_all_common_prefix_empty():
    trie = Trie([])
    common_prefix = trie.get_all_common_prefix('x')
    assert common_prefix == []