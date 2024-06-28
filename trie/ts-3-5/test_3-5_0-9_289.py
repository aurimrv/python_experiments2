import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

def test_initialize_trie():
    words = ["apple", "banana", "application"]
    trie = Trie(words)
    assert len(trie.head) == 2

def test_add_word():
    words = ["apple", "banana"]
    trie = Trie(words)
    trie.add("application")
    assert "a" in trie.head
    assert "p" in trie.head["a"]
    assert trie.head["a"]["p"]["p"]["l"]["i"]["c"]["a"]["t"]["i"]["o"]["n"]["__eof__"] == '__eof__'

def test_get_common_prefix():
    words = ["apple", "banana", "application"]
    trie = Trie(words)
    common_prefixes = trie.get_all_common_prefix("app")
    expected_prefixes = ["apple", "application"]
    assert set(common_prefixes) == set(expected_prefixes)

def test_get_common_prefix_no_match():
    words = ["apple", "banana", "application"]
    trie = Trie(words)
    common_prefixes = trie.get_all_common_prefix("abc")
    assert len(common_prefixes) == 0