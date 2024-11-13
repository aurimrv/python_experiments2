#Pyguin test cases converted from edit-distance/MIO/seed_1706/test_edit_distance.py
import edit_distance as module_0

def test_case_0():
    str_0 = '|WvA'
    var_0 = module_0.calculate_edit_distance(str_0, str_0)

def test_case_1():
    str_0 = ''
    var_0 = module_0.calculate_edit_distance(str_0, str_0)

def test_case_2():
    str_0 = 'I'
    str_1 = '4#KB`8AG]/'
    var_0 = module_0.calculate_edit_distance(str_0, str_1)

def test_case_3():
    str_0 = '['
    str_1 = 'yu'
    var_0 = module_0.calculate_edit_distance(str_1, str_0)
