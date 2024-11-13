#Pyguin test cases converted from radixsort/DYNAMOSA/seed_1706/test_radixsort.py
import pytest
import radixsort as module_0

def test_case_0():
    bytes_0 = b'_\x86j\x18\xbd\xd1]J\xd0\x0c\xb4\x00\xc6h\xaaj\x19\x8f\xc7\xd0'
    var_0 = module_0.radixsort(bytes_0)
    tuple_0 = ()
    var_1 = module_0.radixsort(var_0)

def test_case_1():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]

def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.radixsort(list_0)
