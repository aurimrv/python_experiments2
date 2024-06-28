import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

def test_trie_init():
    words = ['hello', 'world', 'goodbye']
    trie = Trie(words)
    assert trie.head == {'h': {'e': {'l': {'l': {'o': {'__eof__': '__eof__'}}}}}, 'w': {'o': {'r': {'l': {'d': {'__eof__': '__eof__'}}}}}, 'g': {'o': {'o': {'d': {'b': {'y': {'e': {'__eof__': '__eof__'}}}}}}}}

def test_trie_add():
    trie = Trie([])
    trie.add('hello')
    assert trie.head == {'h': {'e': {'l': {'l': {'o': {'__eof__': '__eof__'}}}}}}

    trie.add('world')
    assert trie.head == {'h': {'e': {'l': {'l': {'o': {'__eof__': '__eof__'}}}}}, 'w': {'o': {'r': {'l': {'d': {'__eof__': '__eof__'}}}}}}

def test_get_all_common_prefix():
    words = ['hello', 'world', 'goodbye']
    trie = Trie(words)
    
    prefixes = trie.get_all_common_prefix('he')
    assert prefixes == ['hello']

    prefixes = trie.get_all_common_prefix('w')
    assert prefixes == ['world']

    prefixes = trie.get_all_common_prefix('goo')
    assert prefixes == ['goodbye']

    prefixes = trie.get_all_common_prefix('abc')
    assert prefixes == []