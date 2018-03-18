
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
