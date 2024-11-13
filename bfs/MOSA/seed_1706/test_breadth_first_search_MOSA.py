#Pyguin test cases converted from bfs/MOSA/seed_1706/test_breadth_first_search.py
import pytest
import breadth_first_search as module_0

def test_case_0():
    bytes_0 = b'n\xac\xe20\x1e ='
    set_0 = {bytes_0, bytes_0, bytes_0}

def test_case_1():
    list_0 = []
    var_0 = module_0.breadth_first_search(list_0, list_0, list_0)

def test_case_2():
    none_type_0 = None

def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0]
    var_0 = module_0.breadth_first_search(list_1, list_0, list_1)

def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    list_1 = [list_0]
    var_0 = module_0.breadth_first_search(list_1, list_0, bool_0)
    list_2 = [list_1, list_0, list_1, list_0, list_0]
    var_1 = module_0.breadth_first_search(list_2, list_0, list_1)

def test_case_5():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    list_1 = [list_0]
    var_0 = module_0.breadth_first_search(list_1, list_0, bool_0)
    list_2 = [list_1, list_0, list_1, list_0, list_0]
    var_1 = module_0.breadth_first_search(list_2, list_0, list_1)
    var_2 = module_0.breadth_first_search(list_2, var_0, bool_0)
