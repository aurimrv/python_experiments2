import pytest
from word_squares import word_squares

def test_word_squares_basic():
    assert word_squares(['baba', 'atak', 'abat', 'delt', 'quad']) == [['baba', 'abat', 'baba', 'atak']]

def test_words_squares_multiple_results():
    assert word_squares(['will', 'idle', 'lliw', 'lewd', 'llow']) == [['will', 'idle', 'lliw', 'lewd'], ['will', 'idle', 'llow', 'lewd']]

def test_no_results():
    assert word_squares(['baba', 'free', 'quad', 'high', 'jill']) == []

