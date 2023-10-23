from collections import deque

def bfs(graph, start):
    visited = set()  # Untuk melacak node yang sudah dikunjungi
    queue = deque()  # Gunakan deque sebagai antrian

    queue.append(start)
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Contoh penggunaan:
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D', 'E'],
    'C': ['D', 'E', 'F', 'G'],
    'D': ['E', 'F', 'G'],
    'E': ['F', 'G'],
    'F': ['G'],
    'G': []
}

start_node = 'A'
print("Hasil BFS:")
bfs(graph, start_node)
