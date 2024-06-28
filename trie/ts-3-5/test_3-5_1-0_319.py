import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie

def test_trie_init():
    words = ['apple', 'banana', 'apricot', 'bath']
    trie = Trie(words)
    assert trie.head['a']['p']['p']['l']['e'][Trie.eof] == Trie.eof
    assert trie.head['b']['a']['n']['a']['n']['a'][Trie.eof] == Trie.eof
    assert trie.head['a']['p']['r']['i']['c']['o']['t'][Trie.eof] == Trie.eof
    assert trie.head['b']['a']['t']['h'][Trie.eof] == Trie.eof

def test_trie_add():
    trie = Trie([])
    trie.add('hello')
    trie.add('how')
    trie.add('are')
    trie.add('you')
    assert trie.head['h']['e']['l']['l']['o'][Trie.eof] == Trie.eof
    assert trie.head['h']['o']['w'][Trie.eof] == Trie.eof
    assert trie.head['a']['r']['e'][Trie.eof] == Trie.eof
    assert trie.head['y']['o']['u'][Trie.eof] == Trie.eof

def test_trie_get_all_common_prefix():
    words = ['apple', 'banana', 'apricot', 'bath']
    trie = Trie(words)
    assert trie.get_all_common_prefix('app') == ['apple']
    assert trie.get_all_common_prefix('ban') == ['banana']
    assert trie.get_all_common_prefix('ap') == ['apple', 'apricot']
    assert trie.get_all_common_prefix('bat') == ['bath']