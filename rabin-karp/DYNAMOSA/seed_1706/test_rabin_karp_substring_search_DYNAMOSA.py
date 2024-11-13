#Pyguin test cases converted from rabin-karp/DYNAMOSA/seed_1706/test_rabin_karp_substring_search.py
import pytest
import rabin_karp_substring_search as module_0

def test_case_0():
    str_0 = 'Bod2?F7=\t\r_j{Tix`>'
    var_0 = module_0.rabin_karp_find_substring(str_0, str_0)
    assert var_0 == 0

def test_case_1():
    none_type_0 = None

def test_case_2():
    str_0 = '6\x0b3+'
    str_1 = 'Np\x0cK`m$(lyi?B|yNSv'
    var_0 = module_0.rabin_karp_find_substring(str_1, str_0)
    assert var_0 == -1
