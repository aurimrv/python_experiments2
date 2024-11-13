#Pyguin test cases converted from trie/MOSA/seed_1706/test_trie.py
import pytest
import trie as module_0

def test_case_0():
    str_0 = '/j\n&u(p_*Y6-%*"y5>Q'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'/': {'__eof__': '__eof__'}, 'j': {'__eof__': '__eof__'}, '\n': {'__eof__': '__eof__'}, '&': {'__eof__': '__eof__'}, 'u': {'__eof__': '__eof__'}, '(': {'__eof__': '__eof__'}, 'p': {'__eof__': '__eof__'}, '_': {'__eof__': '__eof__'}, '*': {'__eof__': '__eof__'}, 'Y': {'__eof__': '__eof__'}, '6': {'__eof__': '__eof__'}, '-': {'__eof__': '__eof__'}, '%': {'__eof__': '__eof__'}, '"': {'__eof__': '__eof__'}, 'y': {'__eof__': '__eof__'}, '5': {'__eof__': '__eof__'}, '>': {'__eof__': '__eof__'}, 'Q': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.get_all_common_prefix(str_0)
    trie_1 = module_0.Trie(var_0)
    assert trie_1.head == {}

def test_case_1():
    str_0 = ";8k')N1"
    none_type_0 = None
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {';': {'__eof__': '__eof__'}, '8': {'__eof__': '__eof__'}, 'k': {'__eof__': '__eof__'}, "'": {'__eof__': '__eof__'}, ')': {'__eof__': '__eof__'}, 'N': {'__eof__': '__eof__'}, '1': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.add(str_0)
    assert len(trie_0.head) == 7
    var_1 = trie_0.get_all_common_prefix(str_0)
    trie_1 = module_0.Trie(str_0)
    assert trie_1.head == {';': {'__eof__': '__eof__'}, '8': {'__eof__': '__eof__'}, 'k': {'__eof__': '__eof__'}, "'": {'__eof__': '__eof__'}, ')': {'__eof__': '__eof__'}, 'N': {'__eof__': '__eof__'}, '1': {'__eof__': '__eof__'}}

def test_case_2():
    none_type_0 = None

def test_case_3():
    str_0 = '/j\n&u(p_*Y6-%*"y5>Q'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'/': {'__eof__': '__eof__'}, 'j': {'__eof__': '__eof__'}, '\n': {'__eof__': '__eof__'}, '&': {'__eof__': '__eof__'}, 'u': {'__eof__': '__eof__'}, '(': {'__eof__': '__eof__'}, 'p': {'__eof__': '__eof__'}, '_': {'__eof__': '__eof__'}, '*': {'__eof__': '__eof__'}, 'Y': {'__eof__': '__eof__'}, '6': {'__eof__': '__eof__'}, '-': {'__eof__': '__eof__'}, '%': {'__eof__': '__eof__'}, '"': {'__eof__': '__eof__'}, 'y': {'__eof__': '__eof__'}, '5': {'__eof__': '__eof__'}, '>': {'__eof__': '__eof__'}, 'Q': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.get_all_common_prefix(str_0)
    trie_1 = module_0.Trie(str_0)
    assert trie_1.head == {'/': {'__eof__': '__eof__'}, 'j': {'__eof__': '__eof__'}, '\n': {'__eof__': '__eof__'}, '&': {'__eof__': '__eof__'}, 'u': {'__eof__': '__eof__'}, '(': {'__eof__': '__eof__'}, 'p': {'__eof__': '__eof__'}, '_': {'__eof__': '__eof__'}, '*': {'__eof__': '__eof__'}, 'Y': {'__eof__': '__eof__'}, '6': {'__eof__': '__eof__'}, '-': {'__eof__': '__eof__'}, '%': {'__eof__': '__eof__'}, '"': {'__eof__': '__eof__'}, 'y': {'__eof__': '__eof__'}, '5': {'__eof__': '__eof__'}, '>': {'__eof__': '__eof__'}, 'Q': {'__eof__': '__eof__'}}

def test_case_4():
    list_0 = []
    trie_0 = module_0.Trie(list_0)
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.get_all_common_prefix(list_0)
    var_1 = trie_0.get_all_common_prefix(var_0)
