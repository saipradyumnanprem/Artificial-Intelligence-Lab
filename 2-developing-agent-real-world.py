def addEdge(adj, v, w):
	
	adj[v].append(w)
	adj[w].append(v)
	return adj

def greedyColoring(adj, V):
	
	result = [-1] * V

	result[0] = 0;

	available = [False] * V

	for u in range(1, V):

		for i in adj[u]:
			if (result[i] != -1):
				available[result[i]] = True

		cr = 0
		while cr < V:
			if (available[cr] == False):
				break
			
			cr += 1

		result[u] = cr

		for i in adj[u]:
			if (result[i] != -1):
				available[result[i]] = False
  
  
	for u in range(V):
    
		print("Vertex", u, " ---> Color", result[u])

    
if __name__ == '__main__':
	
	g1 = [[] for i in range(5)]
	g1 = addEdge(g1, 0, 1)
	g1 = addEdge(g1, 0, 2)
	g1 = addEdge(g1, 1, 2)
	g1 = addEdge(g1, 1, 3)
	g1 = addEdge(g1, 2, 3)
	g1 = addEdge(g1, 3, 4)
	print("Coloring of graph:")
	greedyColoring(g1, 5)
