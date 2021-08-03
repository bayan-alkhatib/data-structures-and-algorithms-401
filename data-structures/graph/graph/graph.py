class Node:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, node, weight=0):
        self.node=node
        self.weight=weight


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=0):
        if start_node not in self.adjacency_list or  end_node not in self.adjacency_list:
            return None

        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)

    def get_nodes(self):
        return [key.value for key in self.adjacency_list]

    def get_neighbors(self, node):
        return [(edge.node.value, edge.weight) for edge in self.adjacency_list[node]]


    def size(self):
        return len(self.adjacency_list)



if __name__ == '__main__':
    # graph = Graph()
    # a = graph.add_node('a')
    # b = graph.add_node('b')
    # c = graph.add_node('c')
    # d = graph.add_node('d')
    # e = graph.add_node('e')
    # f = graph.add_node('f')
    # graph.add_edge(a, c)
    # graph.add_edge(a, d)
    # graph.add_edge(b, c)
    # graph.add_edge(b, f)
    # graph.add_edge(c, a)
    # graph.add_edge(c, b)
    # graph.add_edge(c, e)
    # graph.add_edge(d, a)
    # graph.add_edge(d, e)
    # graph.add_edge(e, c)
    # graph.add_edge(e, d)
    # graph.add_edge(e, f)
    # graph.add_edge(f, b)
    # graph.add_edge(f, e)
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a,b,5)
    graph.add_edge(a,c,7)
    expected=[(b,5), (c,7)]
    actual=graph.get_neighbors(a)
    print(actual)



