#Pyguin test cases converted from combinations/MIO/seed_1706/test_combinations.py
import pytest
import combinations as module_0

def test_case_0():
    bytes_0 = b'\r\x93\xb2S\xeb\x83\xa3\x89#\x7f\xf0E\x06gj'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.combinations_of_word(list_0)
    str_0 = 'oY'
    var_1 = module_0.combinations_of_word(var_0)

def test_case_1():
    set_0 = set()
    var_0 = module_0.combinations_of_word(set_0)
    str_0 = 'd`Z#d,7yUfr_'

def test_case_2():
    str_0 = '84'
    str_1 = '6,'
    var_0 = module_0.combinations_of_word(str_1)
    var_1 = module_0.combinations_of_phone_input(str_0)
    var_2 = module_0.combinations_of_phone_input(str_0)
    var_3 = module_0.combinations_of_word(str_0)

def test_case_3():
    str_0 = 'iTe'
