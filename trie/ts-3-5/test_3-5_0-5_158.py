import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

def test_trie_init():
    words = ["apple", "apply", "banana", "bat"]
    trie = Trie(words)
    assert trie.head == {'a': {'p': {'p': {'l': {'e': {'__eof__': '__eof__'}, 'y': {'__eof__': '__eof__'}}}}}, 'b': {'a': {'n': {'a': {'n': {'a': {'__eof__': '__eof__'}}}}, 't': {'__eof__': '__eof__'}}}}

def test_trie_add():
    words = ["apple", "apply", "banana", "bat"]
    trie = Trie(words)
    trie.add("ball")
    assert trie.head == {'a': {'p': {'p': {'l': {'e': {'__eof__': '__eof__'}, 'y': {'__eof__': '__eof__'}}}}}, 'b': {'a': {'n': {'a': {'n': {'a': {'__eof__': '__eof__'}}}}, 't': {'__eof__': '__eof__'}, 'l': {'l': {'__eof__': '__eof__'}}}}}

def test_trie_get_all_common_prefix():
    words = ["apple", "apply", "banana", "bat"]
    trie = Trie(words)
    assert trie.get_all_common_prefix("ba") == ['banana', 'bat']

def test_trie_get_all_common_prefix_no_match():
    words = ["apple", "apply", "banana", "bat"]
    trie = Trie(words)
    assert trie.get_all_common_prefix("xyz") == []

def test_trie_get_all_common_prefix_partial_match():
    words = ["apple", "apply", "banana", "bat"]
    trie = Trie(words)
    assert trie.get_all_common_prefix("ban") == ['banana']

def test_trie_get_all_common_prefix_empty_prefix():
    words = ["apple", "apply", "banana", "bat"]
    trie = Trie(words)
    assert trie.get_all_common_prefix("") == ['apple', 'apply', 'banana', 'bat']