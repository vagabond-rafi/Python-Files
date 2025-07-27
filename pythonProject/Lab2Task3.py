graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['E'],

}
def Abc(graph):
    for i in graph:

     print(i, "has 3 children", graph[i])


Abc(graph)