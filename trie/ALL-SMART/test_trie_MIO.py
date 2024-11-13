#Pyguin test cases converted from trie/MIO/seed_1706/test_trie.py
import pytest
import trie as module_0

def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]

def test_case_1():
    set_0 = set()
    trie_0 = module_0.Trie(set_0)
    assert f'{type(trie_0).__module__}.{type(trie_0).__qualname__}' == 'trie.Trie'
    assert trie_0.head == {}
    assert module_0.Trie.eof == '__eof__'

def test_case_2():
    str_0 = '7f-U8O#"|L'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'7': {'__eof__': '__eof__'}, 'f': {'__eof__': '__eof__'}, '-': {'__eof__': '__eof__'}, 'U': {'__eof__': '__eof__'}, '8': {'__eof__': '__eof__'}, 'O': {'__eof__': '__eof__'}, '#': {'__eof__': '__eof__'}, '"': {'__eof__': '__eof__'}, '|': {'__eof__': '__eof__'}, 'L': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'

def test_case_3():
    str_0 = '&\x0czrJqnF_\\|'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'&': {'__eof__': '__eof__'}, '\x0c': {'__eof__': '__eof__'}, 'z': {'__eof__': '__eof__'}, 'r': {'__eof__': '__eof__'}, 'J': {'__eof__': '__eof__'}, 'q': {'__eof__': '__eof__'}, 'n': {'__eof__': '__eof__'}, 'F': {'__eof__': '__eof__'}, '_': {'__eof__': '__eof__'}, '\\': {'__eof__': '__eof__'}, '|': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.add(str_0)
    assert len(trie_0.head) == 11

def test_case_4():
    set_0 = set()
    trie_0 = module_0.Trie(set_0)
    assert f'{type(trie_0).__module__}.{type(trie_0).__qualname__}' == 'trie.Trie'
    assert trie_0.head == {}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.add(set_0)
    assert trie_0.head == {'__eof__': '__eof__'}

def test_case_5():
    str_0 = '$36TRmS'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'$': {'__eof__': '__eof__'}, '3': {'__eof__': '__eof__'}, '6': {'__eof__': '__eof__'}, 'T': {'__eof__': '__eof__'}, 'R': {'__eof__': '__eof__'}, 'm': {'__eof__': '__eof__'}, 'S': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.get_all_common_prefix(str_0)

def test_case_6():
    str_0 = '&\x0czrJqnF_\\|'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'&': {'__eof__': '__eof__'}, '\x0c': {'__eof__': '__eof__'}, 'z': {'__eof__': '__eof__'}, 'r': {'__eof__': '__eof__'}, 'J': {'__eof__': '__eof__'}, 'q': {'__eof__': '__eof__'}, 'n': {'__eof__': '__eof__'}, 'F': {'__eof__': '__eof__'}, '_': {'__eof__': '__eof__'}, '\\': {'__eof__': '__eof__'}, '|': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.add(str_0)
    assert len(trie_0.head) == 11
    var_1 = trie_0.get_all_common_prefix(str_0)

def test_case_7():
    set_0 = set()
    trie_0 = module_0.Trie(set_0)
    assert f'{type(trie_0).__module__}.{type(trie_0).__qualname__}' == 'trie.Trie'
    assert trie_0.head == {}
    assert module_0.Trie.eof == '__eof__'
    var_0 = trie_0.get_all_common_prefix(set_0)

def test_case_8():
    dict_0 = {}
    str_0 = 'HG'
    trie_0 = module_0.Trie(str_0)
    assert trie_0.head == {'H': {'__eof__': '__eof__'}, 'G': {'__eof__': '__eof__'}}
    assert module_0.Trie.eof == '__eof__'

def test_case_9():
    bool_0 = True
