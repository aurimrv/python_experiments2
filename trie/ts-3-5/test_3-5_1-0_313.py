import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

def test_trie_init_multi_words():
    words = ['apple', 'banana', 'apricot']
    trie = Trie(words)
    assert trie.get_all_common_prefix('a') == ['apple', 'apricot']

def test_trie_add_and_get_all_common_prefix():
    words = ['python', 'java']
    trie = Trie(words)
    trie.add('javascript')
    assert trie.get_all_common_prefix('j') == ['java']

def test_empty_trie_get_all_common_prefix():
    trie = Trie([])
    assert trie.get_all_common_prefix('test') == []

def test_trie_add_special_characters():
    words = ['hello', 'world']
    trie = Trie(words)
    trie.add('@@special##')
    assert trie.get_all_common_prefix('@@') == ['@@special##']

def test_long_word_in_trie():
    words = ['cat', 'dog']
    trie = Trie(words)
    trie.add('grandmother')
    assert trie.get_all_common_prefix('grand') == ['grandmother']