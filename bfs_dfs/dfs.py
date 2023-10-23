graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'B'],
    'D': ['F'],
    'E': ['D', 'F'],
    'F': []
}

visited = set()  # Set untuk melacak node yang sudah dikunjungi

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# Driver Code
dfs(visited, graph, 'A')
