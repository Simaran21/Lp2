#Implementation of BFS in Python ( Breadth First Search


graph = {
'5': ['3', '7'],
'3': ['2','4'],
'7': ['8'],
'2': [],
'4': ['8'],
'8': [],
}
def bfs(graph, initial):
	visited = []
	queue = [initial]
	while queue:
		node = queue.pop(0)
		if node not in visited:
			visited.append(node)
			neighbours = graph[node]

			for neighbour in neighbours:
				queue.append(neighbour)
	return visited
print(bfs(graph,'5'))




#output
"""(base) student@student:~/Documents$ python3 sid.py
['5', '3', '7', '2', '4', '8']
(base) student@student:~/Documents$ 
"""

# DFS algorithm in Python


def dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)

	print(start)

	for next in graph[start] - visited:
		dfs(graph, next, visited)
	return visited

graph = {'0': set(['1', '2']),
'1': set(['0', '3', '4']),
'2': set(['0']),
'3': set(['1']),
'4': set(['2', '3'])}

dfs(graph, '0')

#output
"""(base) student@student:~/Documents$ python3 sid1.py
0
2
1
3
4
(base) student@student:~/Documents$ 
"""
