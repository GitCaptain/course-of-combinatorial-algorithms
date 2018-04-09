
class Graph(dict):

    def __init__(self, nodes, edges):
        for n in nodes:
            self[n] = dict()  # Множества для неповторяющихся элементов
        if edges == None:  # Если все вершины в графе не имеют связей
            pass
        else:
            for e in edges:
                self.add_edge(e)

    def add_edge(self, edge):
        # edge содержит два node,
        # поэтому к вершине A
        # добавим вершину B и наоборот
        self[edge[0]].update({edge[1]: edge[2]})
        self[edge[1]].update({edge[0]: edge[2]})

    def add_node(self, node):
        self[node] = set()

    def get_weight(self, edge):
        return self[edge[0]][edge[1]]

    def __str__(self):
        string = ''
        for key in self.keys():
            string += str(key)
            for item in self[key]:
                 string += '->' + str(item)
            string += '\n'
        return string


def delMin(queue):
    minimum = min(queue, key=queue.get)
    del queue[minimum]
    return minimum


def Prim(graph, start):
    key = {}
    result = {}
    queue = {}

    for v in graph:
        result[v] = -1
        key[v] = 10e3

    key[start] = 0
    for v in graph:
        queue[v] = key[v]

    while queue:
        u = delMin(queue)
        for v in graph[u]:
            if v in queue and graph[u][v] < key[v]:
                result[v] = u
                key[v] = graph[u][v]
                queue[v] = graph[u][v]

    return result


if __name__ == '__main__':
    g_1 = Graph([1, 2, 3, 4, 5, 6], [(1, 2, 10), (2, 3, 2), (3, 4, 5),
                                     (4, 5, 4), (5, 1, 9), (1, 6, 8),
                                     (6, 4, 3), (2, 5, 6), (5, 6, 1)])
    g_2 = Graph([0, 1, 2, 3], [(0, 1, 8), (0, 3, 3), (1, 2, 2),
                               (2, 3, 6), (3, 1, 5)])

    g_3 = Graph([1, 2, 3, 4, 5, 6, 7], [(1, 1, 0), (1, 2, -4), (1, 3, -3), (1, 4, -10), (1, 5, -6), (1, 6, -7), (1, 7, -7),
                                        (2, 2, 0), (2, 3, -5), (2, 4, -4), (2, 5, -4), (2, 6, -3), (2, 7, -9),
                                        (3, 3, 0), (3, 4, -1), (3, 5, -3), (3, 6, -2), (3, 7, -8),
                                        (4, 4, 0), (4, 5, -10), (4, 6, -8), (4, 7, -3),
                                        (5, 5, 0), (5, 6, -4), (5, 7, -5),
                                        (6, 6, 0), (6, 7, -9),
                                        (7, 7, 0)])

    start = 1
    max_tree = Prim(g_3, start)
    max_tree.pop(start)
    understanding = 0
    for u, v in max_tree.items():
        understanding -= g_3[u][v]
    print(max_tree, understanding)
