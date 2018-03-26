

"""
class ListNode:  # односвязный список

    def __init__(self, value=None, nxt=None):
        self.head = self
        self.value = value
        self.next = nxt

    def append(self, value):
        cur = self
        while cur.next:
            cur = cur.next
        cur.next = ListNode(value, None)

    def __str__(self):
        res = str(self.value)
        cur = self
        while cur.next:
            cur = cur.next
            res += '->' + str(cur.value)
        return res


def change_representation(incidence_matrix):
    n = len(incidence_matrix)
    m = len(incidence_matrix[0])

    adjacency_lists = [ListNode(i + 1) for i in range(n)]

    for j in range(m):  # пробегаем по всем ребрам)
        v_from, v_to = -1, -1
        for i in range(n):  # ищем 2 вершины, которым инцидентно ребро
            if incidence_matrix[i][j] == 2:  # петля
                v_from = v_to = i
            if incidence_matrix[i][j] == 1 and v_to == -1:  # ребро j инцидентно вершине i и входит в нее
                v_to = i
            elif incidence_matrix[i][j]:  # ребро j инцидентно вершине i и выходит из нее(для орграфа)
                v_from = i
        adjacency_lists[v_from].append(v_to+1)
        if incidence_matrix[v_to][j] == incidence_matrix[v_from][j] == 1:  # если граф неориентирован добавим еще ребро
            adjacency_lists[v_to].append(v_from+1)

    return adjacency_lists


if __name__ == '__main__':

    n, m = map(int, input('Введите количество строк и столбцов матрицы: ').split())
    print('Введите матрицу инцидентности:')
    matrix = [list(map(int, input().split())) for _ in range(n)]

    res = change_representation(matrix)
    for i in range(len(matrix)):
        print(res[i])
"""


def is_tree(graph):

    n = len(graph)  # количество вершин
    m = 0  # количество ребер
    for node in graph:
        m += len(graph[node])
    m //= 2  # каждое ребро встретилось дважды
    nodes = list(graph.keys())  # получаем все вершины графа
    visited = graph.DFS(nodes[0])[0]  # запускаем DFS из какой-то и получаем массив посещенных вершин

    return all(visited) and n == m + 1


def is_bipartite(graph):
    return graph.DFS(list(graph.keys())[0])[1]


def cycle_exist(graph, edge):
    return graph.BFS(edge[0])[edge[1]] # запустились из edge[0] и не проходя по edge попали в edge[1] -> цикл через edge есть


"""Графы заданы списками смежности"""


# github.com/HigerSkill/
class Graph(dict):

    def __init__(self, nodes, edges):
        for n in nodes:
            self[n] = set() # Множества для неповторяющихся элементов
        if edges == None: # Если все вершины в графе не имеют связей
            pass
        else:
            for e in edges:
                self.add_edge(e)

    def add_edge(self, edge):
        # edge содержит два node,
        # поэтому к вершине A
        # добавим вершину B и наоборот
        self[edge[0]].add(edge[1])
        self[edge[1]].add(edge[0])

    def add_node(self, node):
        self[node] = set()

    def __str__(self):
        string = ''
        for key in self.keys():
            string += str(key)
            for item in self[key]:
                 string += '->' + str(item)
            string += '\n'
        return string

    def BFS(self, s, edge = None):
        # Начинаем обход с вершины s

        visited = [False for _ in range(len(self.items()))]
        queue = [s]
        visited[s] = True

        while queue:
            # Пока очередь не пуста продолжаем обход

            s = queue.pop(0) # Извлекаем вершину
            print(s)

            for w in self[s]:
                # Проанализируем каждую вершину
                if edge and s == edge[0] and w == edge[1]:  # если решаем задачу поиска цикла через ребро, то не идем через это ребро
                    continue
                if visited[w] == False:
                    queue.append(w)
                    visited[w] = True

        return visited

    def DFS(self, s):
        # Начинаем обход с вершины s

        colors = dict()  # цвета вершин
        bipartite = True  # изначально считаем граф двудольным
        colors[s] = 0

        visited = [False for _ in range(len(self.items()))]
        stack = [s]
        visited[s] = True
        while stack:
            # Пока стэк не пуст продолжаем обход

            s = stack.pop()
            print(s)

            for w in self[s]:
                # Проанализируем каждую вершину
                if visited[w] == False:
                    stack.append(w)
                    visited[w] = True
                if colors.get(w) and colors[w] == colors[s]:  # граф раскрасить в два цвета не удалось
                    bipartite = False
                elif not colors.get(w):  # если вершина еще не раскрашена, то красим ее в цвет отличный от ее соседа
                    colors[w] = 1 - colors[s]

        return visited, bipartite


if __name__ == '__main__':
    g = Graph([0,1,2,3,4], [(0, 1), (1, 4), (3, 4), (4, 2), (2, 3)])
    print(is_bipartite(g))
    print(is_tree(g))
    print(cycle_exist(g, (3, 4)))
