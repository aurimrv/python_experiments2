import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

# Test cases for Trie class

def test_trie_init():
    words = ["apple", "banana", "application"]
    trie = Trie(words)
    
def test_trie_add():
    trie = Trie([])
    trie.add("apple")
    trie.add("banana")
    
def test_get_all_common_prefix():
    words = ["apple", "banana", "application"]
    trie = Trie(words)
    prefix = "app"
    common_prefix = trie.get_all_common_prefix(prefix)
    assert "apple" in common_prefix
    assert "application" in common_prefix
    
def test_get_all_common_prefix_empty():
    words = ["apple", "banana", "application"]
    trie = Trie(words)
    prefix = "pea"
    common_prefix = trie.get_all_common_prefix(prefix)
    assert len(common_prefix) == 0