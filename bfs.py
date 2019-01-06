from collections import deque

def bfs(graph, root):
    distance = {}
    distance[root] = 0
    q = deque([root])
    while q:
        current = q.popleft()
        for neighbor in graph[current]