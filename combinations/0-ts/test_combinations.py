import pytest
from combinations import combinations_of_phone_input, combinations_of_word

def test_phone_combo_simple():
    assert combinations_of_phone_input('32') == ['da', 'db', 'dc', 'ea', 'eb', 'ec', 'fa', 'fb', 'fc']

def test_combinations():
    assert combinations_of_word('two') == ['t', 'tw', 'two', 'w', 'wo', 'o']
    assert combinations_of_word('1234') == ['1', '12', '123', '1234', '2', '23', '234', '3', '34', '4']
