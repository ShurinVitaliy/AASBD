import numpy

def find_sequence_of_degrees(graph):
	double_degrees = []
	for node in graph:
		double_degree = 0
		for neighbour in graph[node]:
			double_degree += 1
		double_degrees.append(double_degree)
	return double_degrees

def find_2_sequence_of_degrees(graph):
	double_degree = find_sequence_of_degrees(graph)
	
		
	
	
def find_adjacent_nodes(graph, node):
	nodes = []
	for v in graph:
		if v is node[0]:
			for neighbour in graph[v]:
				nodes.append(neighbour)
		else: 
			continue
		return nodes
	
def is_adjacent_nodes(graph, nodes):
	for i in range(0, len(nodes)):
		adjacent_list = find_adjacent_nodes(graph, nodes[i])
		for j in range(i, len(nodes)):
			if nodes[j] in adjacent_list:
				return True
	return False
			
def is_graph_bipartite(graph):
	list_color1 = []
	list_color2 = []
	i = 0
	for node in graph:
		if node not in list_color2:
			list_color1 += node
			nodes = []
			for neighbour in graph[node]:
				nodes += neighbour
				if neighbour not in list_color2:
					list_color2 += neighbour
			if list_color1[i] in list_color2:
				return False
			if is_adjacent_nodes(graph, nodes):
				return False
			i += 1
	return True
graph = {"a" : ["c"], "b" : ["c", "e"], "c" : ["a", "b", "d", "e"], "d" : ["c"], "e" : ["c", "b"], "f" : []}
print(find_sequence_of_degrees(graph))

bipartite_graph = {"a" : ["d", "e"], "b" : ["d", "e"], "c" : ["d", "e"], "d" : ["a", "b", "c"], "e" : ["a", "b", "c"], "f" : []}
print(is_graph_bipartite(bipartite_graph))
