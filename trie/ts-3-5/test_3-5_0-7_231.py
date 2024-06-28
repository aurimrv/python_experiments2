import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

# Test cases for Trie class
class TestTrie:

    @pytest.fixture
    def trie_instance(self):
        words = ['apple', 'banana', 'grape', 'orange']
        return Trie(words)

    def test_init(self, trie_instance):
        assert trie_instance.head == {'a': {'p': {'p': {'l': {'e': {'__eof__': '__eof__'}}}}}, 
                                      'b': {'a': {'n': {'a': {'n': {'a': {'__eof__': '__eof__'}}}}}}, 
                                      'g': {'r': {'a': {'p': {'e': {'__eof__': '__eof__'}}}}}, 
                                      'o': {'r': {'a': {'n': {'g': {'e': {'__eof__': '__eof__'}}}}}}}

    def test_add(self, trie_instance):
        trie_instance.add('pear')
        assert trie_instance.head == {'a': {'p': {'p': {'l': {'e': {'__eof__': '__eof__'}}}}}, 
                                      'b': {'a': {'n': {'a': {'n': {'a': {'__eof__': '__eof__'}}}}}}, 
                                      'g': {'r': {'a': {'p': {'e': {'__eof__': '__eof__'}}}}}, 
                                      'o': {'r': {'a': {'n': {'g': {'e': {'__eof__': '__eof__'}}}}}},
                                      'p': {'e': {'a': {'r': {'__eof__': '__eof__'}}}}}

    def test_get_all_common_prefix(self, trie_instance):
        assert trie_instance.get_all_common_prefix('ap') == ['apple']
        assert trie_instance.get_all_common_prefix('ban') == ['banana']
        assert trie_instance.get_all_common_prefix('o') == ['orange']
        assert trie_instance.get_all_common_prefix('gr') == ['grape']
