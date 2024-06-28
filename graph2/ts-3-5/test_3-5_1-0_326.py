import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph2 import Graph

def test_add_node():
    g = Graph()
    g.add_node('A')
    assert g.has_node('A')

def test_add_edge():
    g = Graph()
    g.add_node('B')
    g.add_node('C')
    g.add_edge('B', 'C')
    assert g.adjacent('B', 'C')

def test_del_node():
    g = Graph()
    g.add_node('D')
    g.del_node('D')
    assert not g.has_node('D')

def test_del_edge():
    g = Graph()
    g.add_node('E')
    g.add_node('F')
    g.add_edge('E', 'F')
    g.del_edge('E', 'F')
    assert not g.adjacent('E', 'F')

def test_has_node():
    g = Graph()
    g.add_node('G')
    assert g.has_node('G')

def test_neighbors():
    g = Graph()
    g.add_node('H')
    g.add_node('I')
    g.add_edge('H', 'I')
    assert g.neighbors('H') == {'I'}

def test_adjacent():
    g = Graph()
    g.add_node('J')
    g.add_node('K')
    g.add_edge('J', 'K')
    assert g.adjacent('J', 'K')