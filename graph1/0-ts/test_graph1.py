import pytest
from graph1 import Graph
from graph1 import GraphNode
from graph1 import WeightedGraphNode, WeightedGraph

from breadth_first_search import breadth_first_search_graph


def test_non_int():

    graph = Graph(4)

    graph.add_edge('Tampa','Colorado')
    graph.add_edge('Colorado','Las Vegas')
    graph.add_edge('Las Vegas', 'Seattle')
    graph.add_edge('Seattle','Anchorage')

    assert graph.topological_sort() == ['Tampa', 'Colorado', 'Las Vegas', 'Seattle', 'Anchorage']


def test_cycles_true():

    graph = Graph(4)

    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,0)

    assert graph.has_cycle() == True


def test_cycles_true_complex_graph():

    graph = Graph(7)

    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(3,2)
    graph.add_edge(4,3)
    graph.add_edge(4,6)
    graph.add_edge(5,3)
    graph.add_edge(5,4)
    graph.add_edge(6,5)

    assert graph.has_cycle() == True


def test_cycles_true_2_node_graph():

    graph = Graph(2)

    graph.add_edge(0,1)
    graph.add_edge(1,0)

    assert graph.has_cycle() == True


def test_cycle_with_discrete_forest():

    graph = Graph(6)

    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(5,3)

    assert graph.has_cycle() == True


def test_cycles_false():

    graph = Graph(4)

    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)

    assert graph.has_cycle() == False


def test_too_many_verticies_error():

    graph = Graph(1)

    graph.add_edge(0,1)
    with pytest.raises(IndexError):
        graph.add_edge(1,2)


def test_graph_node():
    assert GraphNode(4).val == 4


def test_insert():
    node = GraphNode(1)

    two = GraphNode(2)
    three = GraphNode(3)
    node.add_adjacent(two)

    assert two in node.adjacent_list
    assert three not in node.adjacent_list

    three.add_adjacent(three)

    assert two in node.adjacent_list


def test_delete():
    node = GraphNode(1)
    two = GraphNode(2)
    node.add_adjacent(two)

    node.remove_adjacent(two)

    assert two not in node.adjacent_list

    with pytest.raises(KeyError):
        node.remove_adjacent(GraphNode(1))

##########################
### test_graph_bsf
##########################
def make_graph():
    head = GraphNode(0)
    one = GraphNode(1)
    two = GraphNode(2)
    three = GraphNode(3)
    four = GraphNode(4)

    head.add_adjacent(one)
    head.add_adjacent(two)

    one.add_adjacent(three)

    two.add_adjacent(four)

    four.add_adjacent(two)

    return head


def make_long_graph():
    head = GraphNode(0)
    one = GraphNode(1)
    two = GraphNode(2)
    three = GraphNode(3)
    four = GraphNode(4)
    five = GraphNode(5)
    six = GraphNode(6)

    head.add_adjacent(one)
    head.add_adjacent(two)

    one.add_adjacent(three)

    two.add_adjacent(four)

    four.add_adjacent(two)
    four.add_adjacent(five)

    five.add_adjacent(six)

    return head


def test_basic_graph_bfs():
    head = make_graph()

    assert breadth_first_search_graph(head, 3).val == 3


def test_not_found():
    assert breadth_first_search_graph(make_graph(), 8) is None


def test_with_adjacency_circle():
    assert breadth_first_search_graph(make_long_graph(), 6).val == 6


###########################
# test_topological_sort
###########################

def test_topological_sort():
    graph = Graph(6)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)

    graph.add_edge(4, 0)
    graph.add_edge(4, 1)

    graph.add_edge(2, 3)

    graph.add_edge(3, 1)

    assert graph.topological_sort() == [4, 5, 0, 2, 3, 1]



##############################
# test_weighted_graph
#############################

def test_add_vertex():

    graph = WeightedGraph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')

    assert ['a','b','c'] == list(graph.vertices.keys())
    
def test_add_edge():

    graph = WeightedGraph()

    graph.add_edge('a','b',1)
    graph.add_edge('a','c',3)
    graph.add_edge('b','c',2)

    assert {'b':1,'c':3} == graph.vertices['a'].adjacent

    assert {'c':2} == graph.vertices['b'].adjacent

def test_remove_adjacent():

    graph = WeightedGraph()

    graph.add_edge('a','b',2)

    graph.remove_edge('a','b')

    graph.remove_edge('a','c')

    graph.remove_edge('c','a')

    assert {} == graph.vertices['a'].adjacent

def test_print_graph():
    graph = WeightedGraph()

    graph.add_edge('a','b',1)
    graph.add_edge('a','c',3)
    graph.add_edge('b','c',2)

    assert "a adjacent: ['b', 'c'], b adjacent: ['c'], c adjacent: []" == graph.__str__()

