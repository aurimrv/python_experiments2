import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph2 import Graph

# Test cases for Graph class methods

def test_add_node():
    g = Graph()
    g.add_node('A')
    assert 'A' in g.nodes()

def test_add_edge():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B')
    assert 'B' in g.neighbors('A')

def test_del_node():
    g = Graph()
    g.add_node('A')
    g.del_node('A')
    assert 'A' not in g.nodes()

def test_del_edge():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B')
    g.del_edge('A', 'B')
    assert 'B' not in g.neighbors('A')

def test_has_node():
    g = Graph()
    g.add_node('A')
    assert g.has_node('A') == True

def test_neighbors():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B')
    assert 'B' in g.neighbors('A')

def test_adjacent():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B')
    assert g.adjacent('A', 'B') == True
