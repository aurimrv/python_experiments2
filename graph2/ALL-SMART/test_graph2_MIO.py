#Pyguin test cases converted from graph2/MIO/seed_1706/test_graph2.py
import pytest
import graph2 as module_0

def test_case_0():
    str_0 = 'O*s,\nTBbojY-'
    graph_0 = module_0.Graph(str_0)
    assert graph_0.graph == {'O': {*()}, '*': {*()}, 's': {*()}, ',': {*()}, '\n': {*()}, 'T': {*()}, 'B': {*()}, 'b': {*()}, 'o': {*()}, 'j': {*()}, 'Y': {*()}, '-': {*()}}

def test_case_1():
    float_0 = 1100.3594

def test_case_2():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}

def test_case_3():
    str_0 = 'O*?s,\nTBbo$jY-'
    graph_0 = module_0.Graph(str_0)
    assert graph_0.graph == {'O': {*()}, '*': {*()}, '?': {*()}, 's': {*()}, ',': {*()}, '\n': {*()}, 'T': {*()}, 'B': {*()}, 'b': {*()}, 'o': {*()}, '$': {*()}, 'j': {*()}, 'Y': {*()}, '-': {*()}}
    var_0 = graph_0.edges()

def test_case_4():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.edges()

def test_case_5():
    bytes_0 = b'\xe8\xc9\xe5'
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.add_node(graph_0)
    var_1 = graph_0.add_edge(graph_0, graph_0)
    var_2 = graph_0.add_node(bytes_0)
    var_3 = graph_0.edges()

def test_case_6():
    bytes_0 = b'R?'
    none_type_0 = None
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.add_edge(none_type_0, none_type_0)
    var_1 = graph_0.add_edge(bytes_0, bytes_0)
    var_2 = graph_0.del_node(bytes_0)

def test_case_7():
    bytes_0 = b'R?'
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.add_edge(bytes_0, bytes_0)
    var_1 = graph_0.del_node(bytes_0)

def test_case_8():
    bytes_0 = b'R?'
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.nodes()

def test_case_9():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}

def test_case_10():
    int_0 = -857
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.has_node(int_0)
    assert var_0 is False

def test_case_11():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
