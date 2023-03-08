import pytest
from dijkstras import dijkstras
from graph import WeightedGraph

def test_basic_dij():
    graph = WeightedGraph()

    graph.add_edge('a','b',1)
    graph.add_edge('a','c',4)
    graph.add_edge('b','c',2)

    assert dijkstras(graph,'a','c') == ['a','b','c']

def test_advanced_dij():
    graph = WeightedGraph()

    graph.add_edge('1','2',7)
    graph.add_edge('1','3',9)
    graph.add_edge('1','6',14)
    graph.add_edge('2','3',10)
    graph.add_edge('2','4',15)
    graph.add_edge('3','4',11)
    graph.add_edge('3','6',2)
    graph.add_edge('4','5',6)
    graph.add_edge('6','5',9)

    assert dijkstras(graph,'1','5') == ['1','3','6','5']

