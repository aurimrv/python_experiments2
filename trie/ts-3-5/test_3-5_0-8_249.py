import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from trie import Trie

class TestTrie:

    def test_init_single_word(self):
        words = ["apple"]
        trie = Trie(words)
        assert trie.get_all_common_prefix("a") == ["apple"]

    def test_init_multiple_words(self):
        words = ["apple", "banana", "orange"]
        trie = Trie(words)
        assert trie.get_all_common_prefix("b") == ["banana"]

    def test_add_word(self):
        trie = Trie([])
        trie.add("hello")
        assert trie.get_all_common_prefix("h") == ["hello"]

    def test_get_all_common_prefix_exists(self):
        words = ["apple", "banana", "orange"]
        trie = Trie(words)
        assert trie.get_all_common_prefix("b") == ["banana"]
  
    def test_get_all_common_prefix_nonexistent(self):
        words = ["apple", "banana", "orange"]
        trie = Trie(words)
        assert trie.get_all_common_prefix("z") == []

    def test_get_all_common_prefix_empty_trie(self):
        trie = Trie([])
        assert trie.get_all_common_prefix("a") == []

    def test_get_all_common_prefix_empty_input(self):
        words = ["apple", "banana", "orange"]
        trie = Trie(words)
        assert trie.get_all_common_prefix("") == ["apple", "banana", "orange"]