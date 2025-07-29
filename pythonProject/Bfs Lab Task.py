graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': ['P'],
    'H': [],
    'P': []
}
def bfs(graph):
    explored = []
    queue = ['A']
    parent = {}
    for i in queue:
        if i not in explored:
            print(i, end=' ')
            explored.append(i)
            for neighbor in graph[i]:
                if neighbor not in parent:
                    parent[neighbor] = i
            queue += graph[i]


    path = []
    current = 'P'
    while current in parent or current == 'A':
        path.append(current)
        if current == 'A':
            break
        current = parent [current]
    path.reverse()

    print("")
    print("Shortest path from A to P:", path)

bfs(graph)
