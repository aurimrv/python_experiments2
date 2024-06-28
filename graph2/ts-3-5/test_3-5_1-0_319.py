import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from graph2 import Graph

@pytest.fixture
def graph_instance():
    return Graph()

def test_initial_empty_nodes(graph_instance):
    assert graph_instance.nodes() == []

def test_add_node(graph_instance):
    graph_instance.add_node('A')
    assert 'A' in graph_instance.nodes()

def test_add_duplicate_node(graph_instance):
    graph_instance.add_node('B')
    graph_instance.add_node('B')
    assert len(graph_instance.nodes()) == 1

def test_add_edge(graph_instance):
    graph_instance.add_node('C')
    graph_instance.add_node('D')
    graph_instance.add_edge('C', 'D')
    assert 'D' in graph_instance.neighbors('C')

def test_del_node(graph_instance):
    graph_instance.add_node('E')
    graph_instance.del_node('E')
    assert 'E' not in graph_instance.nodes()

def test_del_edge(graph_instance):
    graph_instance.add_node('F')
    graph_instance.add_node('G')
    graph_instance.add_edge('F', 'G')
    graph_instance.del_edge('F', 'G')
    assert 'G' not in graph_instance.neighbors('F')