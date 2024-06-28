import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

def test_init():
    words = ['apple', 'orange', 'banana']
    trie = Trie(words)
    assert trie.head == {'a': {'p': {'p': {'l': {'e': {'__eof__': '__eof__'}}}}}, 
                         'o': {'r': {'a': {'n': {'g': {'e': {'__eof__': '__eof__'}}}}}, 
                               'r': {'a': {'n': {'g': {'e': {'__eof__': '__eof__'}}}}}}, 
                         'b': {'a': {'n': {'a': {'n': {'a': {'__eof__': '__eof__'}}}}}}}

def test_add():
    words = ['apple', 'orange', 'banana']
    trie = Trie(words)
    
    trie.add('kiwi')
    assert trie.head == {'a': {'p': {'p': {'l': {'e': {'__eof__': '__eof__'}}}}}, 
                         'o': {'r': {'a': {'n': {'g': {'e': {'__eof__': '__eof__'}}}}}, 
                               'r': {'a': {'n': {'g': {'e': {'__eof__': '__eof__'}}}}}}, 
                         'b': {'a': {'n': {'a': {'n': {'a': {'__eof__': '__eof__'}}}}}},
                         'k': {'i': {'w': {'i': {'__eof__': '__eof__'}}}}}

def test_get_all_common_prefix():
    words = ['apple', 'orange', 'banana']
    trie = Trie(words)
    
    assert trie.get_all_common_prefix('app') == ['apple']
    assert trie.get_all_common_prefix('or') == ['orange']
    assert trie.get_all_common_prefix('ban') == ['banana']

    trie.add('appetizer')
    assert trie.get_all_common_prefix('app') == ['apple', 'appetizer']