#Pyguin test cases converted from graph1/MOSA/seed_1706/test_graph1.py
import pytest
import graph1 as module_0
import collections as module_1
import builtins as module_2

def test_case_0():
    weighted_graph_0 = module_0.WeightedGraph()
    graph_0 = module_0.Graph(weighted_graph_0)
    var_0 = graph_0.topological_sort()

def test_case_1():
    int_0 = -3753
    weighted_graph_node_0 = module_0.WeightedGraphNode(int_0)
    var_0 = weighted_graph_node_0.__str__()
    assert var_0 == '-3753 adjacent: []'
    set_0 = set()
    weighted_graph_node_1 = module_0.WeightedGraphNode(int_0)
    var_1 = weighted_graph_node_1.add_adjacent(int_0)
    assert weighted_graph_node_1.adjacent == {-3753: 0}

def test_case_2():
    defaultdict_0 = module_1.defaultdict()
    none_type_0 = None
    deque_0 = module_1.deque()
    int_0 = -1673
    weighted_graph_0 = module_0.WeightedGraph()
    var_0 = weighted_graph_0.add_edge(none_type_0, none_type_0)
    var_1 = weighted_graph_0.__str__()
    assert var_1 == 'None adjacent: [None]'

def test_case_3():
    weighted_graph_0 = module_0.WeightedGraph()
    graph_0 = module_0.Graph(weighted_graph_0)
    var_0 = weighted_graph_0.__str__()

def test_case_4():
    weighted_graph_0 = module_0.WeightedGraph()
    none_type_0 = None
    var_0 = weighted_graph_0.add_edge(weighted_graph_0, none_type_0, weighted_graph_0)
    assert len(weighted_graph_0.vertices) == 2
    graph_0 = module_0.Graph(weighted_graph_0)
    var_1 = graph_0.topological_sort()
    bytes_0 = b'#\x07\xc7&\xd5\xa3A\xc4'
    graph_node_0 = module_0.GraphNode(bytes_0)

def test_case_5():
    none_type_0 = None
    weighted_graph_0 = module_0.WeightedGraph()
    var_0 = weighted_graph_0.add_edge(none_type_0, none_type_0, weighted_graph_0)
    var_1 = weighted_graph_0.add_edge(none_type_0, none_type_0, none_type_0)

def test_case_6():
    str_0 = '#?0-U8+r3r0YbzTNvJ'
    weighted_graph_0 = module_0.WeightedGraph()
    var_0 = weighted_graph_0.remove_edge(str_0, str_0)
    var_1 = weighted_graph_0.__str__()
    bytes_0 = b'\xba\xc1\xce\xcd\xae&\xfamb\x13\x05\x93\xe4\xc0\x11`\x93H|\x9a'
    graph_0 = module_0.Graph(bytes_0)

def test_case_7():
    weighted_graph_0 = module_0.WeightedGraph()

def test_case_8():
    object_0 = module_2.object()
    graph_node_0 = module_0.GraphNode(object_0)
    var_0 = graph_node_0.add_adjacent(object_0)

def test_case_9():
    weighted_graph_0 = module_0.WeightedGraph()
    graph_0 = module_0.Graph(weighted_graph_0)
    var_0 = graph_0.topological_sort()
    bytes_0 = b'#\x07\xc7&\xd5\xa3A\xc4'
    graph_node_0 = module_0.GraphNode(bytes_0)

def test_case_10():
    weighted_graph_0 = module_0.WeightedGraph()
    var_0 = weighted_graph_0.add_vertex(weighted_graph_0)
    tuple_0 = (var_0, var_0, var_0)

def test_case_11():
    int_0 = -524
    complex_0 = 599 - 661.7138j
    weighted_graph_node_0 = module_0.WeightedGraphNode(complex_0)

def test_case_12():
    weighted_graph_0 = module_0.WeightedGraph()
    weighted_graph_node_0 = module_0.WeightedGraphNode(weighted_graph_0)
    none_type_0 = None
    var_0 = weighted_graph_0.add_edge(weighted_graph_0, none_type_0, weighted_graph_0)
    assert len(weighted_graph_0.vertices) == 2
    graph_0 = module_0.Graph(weighted_graph_0)
    var_1 = graph_0.topological_sort()
    var_2 = var_0.__str__()
    var_3 = weighted_graph_0.remove_edge(none_type_0, none_type_0)

def test_case_13():
    weighted_graph_0 = module_0.WeightedGraph()
    var_0 = weighted_graph_0.remove_edge(weighted_graph_0, weighted_graph_0)
    none_type_0 = None
    var_1 = weighted_graph_0.add_edge(weighted_graph_0, none_type_0, weighted_graph_0)
    assert len(weighted_graph_0.vertices) == 2
    graph_0 = module_0.Graph(weighted_graph_0)
    var_2 = graph_0.topological_sort()
    var_3 = var_1.__str__()
    var_4 = weighted_graph_0.remove_edge(none_type_0, graph_0)

def test_case_14():
    weighted_graph_0 = module_0.WeightedGraph()
    weighted_graph_node_0 = module_0.WeightedGraphNode(weighted_graph_0)
    none_type_0 = None
    list_0 = []
    var_0 = weighted_graph_0.add_edge(none_type_0, none_type_0, list_0)
    graph_0 = weighted_graph_0.remove_edge(var_0, var_0)

def test_case_15():
    bool_0 = False
    graph_0 = module_0.Graph(bool_0)
    none_type_0 = None
    var_0 = graph_0.has_cycle()
    assert var_0 is False

def test_case_16():
    int_0 = 23
    graph_0 = module_0.Graph(int_0)
    var_0 = graph_0.add_edge(graph_0, graph_0)
    assert len(graph_0.graph) == 1

def test_case_17():
    int_0 = 23
    graph_0 = module_0.Graph(int_0)
    graph_node_0 = module_0.GraphNode(int_0)
    var_0 = graph_0.add_edge(int_0, graph_node_0)
    assert len(graph_0.graph) == 2
    graph_1 = module_0.Graph(graph_node_0)

def test_case_18():
    int_0 = 0
    graph_0 = module_0.Graph(int_0)
    none_type_0 = None
    weighted_graph_node_0 = module_0.WeightedGraphNode(none_type_0)
    var_0 = graph_0.add_edge(none_type_0, none_type_0)
    assert graph_0.graph == {None: [None]}
    with pytest.raises(IndexError):
        graph_0.add_edge(var_0, var_0)

def test_case_19():
    int_0 = 23
    graph_0 = module_0.Graph(int_0)

def test_case_20():
    int_0 = 23
    graph_0 = module_0.Graph(int_0)
    none_type_0 = None
    bool_0 = False
    var_0 = graph_0.add_edge(none_type_0, bool_0)
    assert graph_0.graph == {None: [False], False: []}
    var_1 = var_0.__str__()
    var_2 = var_1.__str__()
    var_3 = graph_0.topological_sort()
    var_4 = graph_0.add_edge(none_type_0, none_type_0)
    graph_1 = module_0.Graph(var_4)

def test_case_21():
    bool_0 = True
    weighted_graph_node_0 = module_0.WeightedGraphNode(bool_0)
    int_0 = 23
    graph_0 = module_0.Graph(int_0)
    var_0 = graph_0.topological_sort()
    bool_1 = False
    var_1 = graph_0.add_edge(bool_1, bool_1)
    assert graph_0.graph == {False: [False]}
    var_2 = graph_0.topological_sort()
    var_3 = graph_0.add_edge(bool_1, bool_1)
    assert graph_0.graph == {False: [False, False]}
    graph_1 = module_0.Graph(var_3)
    var_4 = graph_0.has_cycle()
    assert var_4 is True
    weighted_graph_0 = module_0.WeightedGraph()

def test_case_22():
    bool_0 = True
    int_0 = 23
    graph_0 = module_0.Graph(int_0)
    bool_1 = False
    var_0 = graph_0.add_edge(bool_0, bool_1)
    assert graph_0.graph == {True: [False], False: []}
    var_1 = graph_0.topological_sort()
    graph_1 = module_0.Graph(var_1)
    assert graph_1.verticies == [True, False]

def test_case_23():
    bool_0 = False
    int_0 = 23
    graph_0 = module_0.Graph(int_0)
    bool_1 = True
    var_0 = graph_0.add_edge(bool_0, bool_1)
    assert graph_0.graph == {False: [True], True: []}
    var_1 = graph_0.topological_sort()
    graph_1 = module_0.Graph(var_1)
    assert graph_1.verticies == [False, True]
