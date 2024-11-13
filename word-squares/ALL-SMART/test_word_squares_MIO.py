#Pyguin test cases converted from word-squares/MIO/seed_1706/test_word_squares.py
import pytest
import word_squares as module_0

def test_case_0():
    str_0 = 'EL#1$Tjgcv\\,'
    var_0 = module_0.word_squares(str_0)

def test_case_1():
    str_0 = '66dX)@eym<pVRwIO+3#='
    list_0 = [str_0, str_0]
    var_0 = module_0.word_squares(list_0)
    var_1 = module_0.word_squares(list_0)
    var_2 = module_0.word_squares(list_0)
    var_3 = module_0.word_squares(str_0)
    var_4 = module_0.word_squares(str_0)
    var_5 = module_0.word_squares(var_4)
    var_6 = module_0.word_squares(str_0)

def test_case_2():
    str_0 = 'EL#1#jgcv\\,'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.word_squares(dict_0)

def test_case_3():
    bool_0 = True
