"""
Inputs...
dependency = {
    [otherfile, otherfile2],
    [somefile1, somefile2]
    ...
}
root_file
"""

def _build_graph(dependencies, root_file):
    """" Returns a adjicent list representing the graph """

def _next_0_degree_node(graph):
    """ Returns the node with 0 in degree from the graph, or None"""

def _remove_node_from_graph(graph):
    """ Mutates and removes the node from the graph (adjicent list)"""


def get_dependencies_ordering(dependencies, root_file):
    # Do a topological sort
    node_ordering = []                              # We'll return this
    graph = _build_graph(dependencies, root_file)   # Build adjcency list from the graph

    # Toplogical sort:
    # remove nodes with in-degree of 0
    #   add removed onto dependency ordering
    #   remove it from the graph
    node_zero_in_degree = _next_0_degree_node(graph)

    if node_zero_in_degree == None:                 # Won't work if there's a loop
        return node_ordering
    else:
        node_ordering = [node_zero_in_degree]

    while node_zero_in_degree is not None:
        node_ordering.append(node_zero_in_degree)
        _remove_node_from_graph(graph)
        node_zero_in_degree = _next_0_degree_node(graph)

    return node_ordering