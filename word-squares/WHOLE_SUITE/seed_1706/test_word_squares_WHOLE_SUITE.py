#Pyguin test cases converted from word-squares/WHOLE_SUITE/seed_1706/test_word_squares.py
import pytest
import word_squares as module_0
import trie as module_1
import builtins as module_2

def test_case_0():
    none_type_0 = None

def test_case_1():
    str_0 = 'X>Si=N#$Oh'
    var_0 = module_0.word_squares(str_0)
    var_1 = module_0.word_squares(var_0)
    dict_0 = {str_0: str_0}
    var_2 = module_0.word_squares(dict_0)
    dict_1 = {}
    var_3 = module_0.word_squares(dict_1)

def test_case_2():
    bytes_0 = b'L\x86\xbeH\xea\xd3\x17\x129\x07\x8f\xeb\xc3_\xfc.'

def test_case_3():
    str_0 = 'd6w69NfK~~}&\t,Q'
    trie_0 = module_1.Trie(str_0)
    var_0 = module_0.word_squares(str_0)
    none_type_0 = None
    dict_0 = {str_0: none_type_0}
    var_1 = module_0.word_squares(dict_0)
    var_2 = module_0.word_squares(var_1)
    var_3 = module_0.word_squares(var_2)
    object_0 = module_2.object(*var_2)

def test_case_4():
    str_0 = '[[4.nvZ'
    set_0 = {str_0, str_0, str_0, str_0}
    var_0 = module_0.word_squares(set_0)

def test_case_5():
    bool_0 = False
