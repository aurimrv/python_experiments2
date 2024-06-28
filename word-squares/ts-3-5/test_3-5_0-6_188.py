import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from trie import Trie
from word_squares import word_squares

def test_construct():
    words = ['ball', 'area', 'lead', 'lady']
    squares = word_squares(words)
    assert len(squares) == 1
    assert squares == [['ball', 'area', 'lead', 'lady']]

def test_construct_single_word():
    words = ['hello']
    squares = word_squares(words)
    assert len(squares) == 0
    assert squares == []

def test_construct_empty_input():
    words = []
    squares = word_squares(words)
    assert squares == []

def test_construct_long_words():
    words = ['python', 'testing', 'mutation', 'senior']
    squares = word_squares(words)
    assert len(squares) == 0

def test_construct_repeated_words():
    words = ['apple', 'apple', 'apple']
    squares = word_squares(words)
    assert len(squares) == 0