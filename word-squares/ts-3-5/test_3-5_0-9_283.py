import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from word_squares import word_squares

@pytest.fixture
def words():
    return ["ball", "area", "lead", "lady"]

def test_construct_single_square(words):
    assert word_squares(words) == [['ball', 'area', 'lead', 'lady']]

def test_construct_multiple_squares(words):
    assert len(word_squares(words)) == 1

def test_construct_empty_list():
    assert word_squares([]) == []

def test_construct_no_squares(words):
    assert word_squares(["hello", "world"]) == []

def test_construct_duplicate_words(words):
    assert len(word_squares(["ball", "ball", "area", "lead", "lady"])) == 2