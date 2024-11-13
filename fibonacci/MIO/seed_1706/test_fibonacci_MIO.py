#Pyguin test cases converted from fibonacci/MIO/seed_1706/test_fibonacci.py
import pytest
import fibonacci as module_0

def test_case_0():
    bool_0 = False
    int_0 = 2334
    var_0 = module_0.fibonacci_dp(int_0)
    assert var_0 == 26771169346070112008973137686107242013910215317383976458597665974368809338804008268575831123149220921300211278402955917456419369066496527715637613116343630271971657798712975711782131938422369220396742173064184881356676581692970189511096814290883903746410403622906847597768914774066168903647391330130495669581320411418251766772991287299334743771638148461363053731309693794558158940302767940991219726533288998391028064372800927768103579932020779318137038888384614853035717263484776560655912
    none_type_0 = None
    var_1 = module_0.fibonacci_recursive(bool_0)
    assert var_1 == 0

def test_case_1():
    bool_0 = True
    var_0 = module_0.fibonacci_dp(bool_0)
    assert var_0 == 1
    var_1 = module_0.fibonacci_dp(var_0)
    assert var_1 == 1

def test_case_2():
    int_0 = -1244
    var_0 = module_0.fibonacci_recursive(int_0)
    assert var_0 == 0
    var_1 = module_0.fibonacci_dp(var_0)
    assert var_1 == 0
    int_1 = 1483
    int_2 = -540
    var_2 = module_0.fibonacci_recursive(int_2)
    assert var_2 == 0

def test_case_3():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.fibonacci_recursive(bool_0)
    assert var_0 == 0

def test_case_4():
    int_0 = 2847
