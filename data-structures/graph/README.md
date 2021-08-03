# Graphs
 Graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges

## Challenge

- to create 3 classes (vertix , edge , graph)
- vertix is suck like a Node class
- edge which a class to create a relation between the nodes
- graph class that connect the edges with the nodes and it has a methods that helps to show the data and add it


## Approach & Efficiency
- add_node: time O(1), space O(1)
- add_edge:time O(n), space O(n)
- get_nodes:time O(n), space O(n)
- get_neighbors:time O(n), space O(n)
- size:time O(1), space O(1)

## API

- add_node(value): adds a new node to the graph, returns the added node
- add_edge(start_node, end_node, weight): adds new edge between two nodes, takes in two nodes, has ability to add weight
- get_nodes( ) - returns all of the nodes as a collection
- get_neighbors(node): returns a collection of nodes (with weights) connected to a node, takes in a node
- size( ):  returns number of nodes in Graph; integer

