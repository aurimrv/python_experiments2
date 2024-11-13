#Pyguin test cases converted from trie/DYNAMOSA/seed_1706/test_trie.py
import pytest
import trie as module_0
import builtins as module_1

def test_case_0():
    str_0 = '&\x0czrJqnF_\\|'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'&': {'__eof__': '__eof__'}, '\x0c': {'__eof__': '__eof__'}, 'z': {'__eof__': '__eof__'}, 'r': {'__eof__': '__eof__'}, 'J': {'__eof__': '__eof__'}, 'q': {'__eof__': '__eof__'}, 'n': {'__eof__': '__eof__'}, 'F': {'__eof__': '__eof__'}, '_': {'__eof__': '__eof__'}, '\\': {'__eof__': '__eof__'}, '|': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.add(str_0)
    assert len(trie_0.head) == 11
    var_1 = trie_0.get_all_common_prefix(str_0)

def test_case_1():
    none_type_0 = None

def test_case_2():
    list_0 = []
    trie_0 = module_0.Trie(list_0)
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.get_all_common_prefix(list_0)

def test_case_3():
    list_0 = []
    trie_0 = module_0.Trie(list_0)
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.get_all_common_prefix(list_0)
    str_0 = '/j\n&u(p_*Y6-%*"y5>Q'
    trie_1 = module_0.Trie(str_0)
    assert trie_1.head == {'/': {'__eof__': '__eof__'}, 'j': {'__eof__': '__eof__'}, '\n': {'__eof__': '__eof__'}, '&': {'__eof__': '__eof__'}, 'u': {'__eof__': '__eof__'}, '(': {'__eof__': '__eof__'}, 'p': {'__eof__': '__eof__'}, '_': {'__eof__': '__eof__'}, '*': {'__eof__': '__eof__'}, 'Y': {'__eof__': '__eof__'}, '6': {'__eof__': '__eof__'}, '-': {'__eof__': '__eof__'}, '%': {'__eof__': '__eof__'}, '"': {'__eof__': '__eof__'}, 'y': {'__eof__': '__eof__'}, '5': {'__eof__': '__eof__'}, '>': {'__eof__': '__eof__'}, 'Q': {'__eof__': '__eof__'}}

def test_case_4():
    str_0 = '&\x0czrJqnF_\\|'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'&': {'__eof__': '__eof__'}, '\x0c': {'__eof__': '__eof__'}, 'z': {'__eof__': '__eof__'}, 'r': {'__eof__': '__eof__'}, 'J': {'__eof__': '__eof__'}, 'q': {'__eof__': '__eof__'}, 'n': {'__eof__': '__eof__'}, 'F': {'__eof__': '__eof__'}, '_': {'__eof__': '__eof__'}, '\\': {'__eof__': '__eof__'}, '|': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.get_all_common_prefix(str_0)
