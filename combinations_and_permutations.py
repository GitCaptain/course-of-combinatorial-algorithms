
def comb(n, k):
    A = []
    B = [i+1 for i in range(k)]

    if n == k:
        return [B]
    elif n < k:
        return False

    p = k
    while p >= 0:
        A.append(B.copy())
        p = p-1 if B[k-1] == n else k-1
        if p >= 0:
            for i in range(k-1, p-1, -1):
                B[i] = B[p] + i - p + 1

    return A


def permut(n):
    A = []
    B = [i+1 for i in range(n)]

    if n == 0:
        return [[0]]
    elif n < 0:
        return False

    while True:
        A.append(B.copy())
        i = n-2

        while i != -1 and B[i] >= B[i+1]:
            i = i-1

        if i == -1:
            break

        k = n-1
        while B[i] >= B[k]:
            k = k-1

        B[i], B[k] = B[k], B[i]
        B[i+1:n] = reversed(B[i+1:n])

    return A


def solve_rhomb():
    from math import sqrt
    get_len_sqr = lambda p1, p2: (p1[0]-p2[0])**2+(p1[1]-p2[1])**2  # квадрат расстояния между точками p1, p2
    scalar_product = lambda v1, v2: v1[0]*v2[0] + v1[1]*v2[1]  # скалярное произведение
    permutations = permut(4)

    def rhomb_square(cur_points):
        for permut in permutations:
            p1, p2, p3, p4 = [cur_points[permut[i]-1] for i in range(4)]
            if p1 == p2 == p3 == p4:
                # вырожденный ромб - не ромб
                continue
            if not get_len_sqr(p1, p2) == get_len_sqr(p2, p3) == get_len_sqr(p3, p4) == get_len_sqr(p4, p1):
                # все стороны ромба должны быть равны между собой
                continue
            v1 = (p3[0] - p1[0], p3[1] - p1[1])  # диагонали ромба
            v2 = (p2[0] - p4[0], p2[1] - p4[1])
            if scalar_product(v1, v2):
                # Диагонали должны быть перпендикулярны, т.е. скалярное произведение = 0
                continue
            # Если все условия выполнены, значит ромб, возвращаем его площадь
            return sqrt(get_len_sqr(p1, p3))*sqrt(get_len_sqr(p2, p4))/2
        # ни одна перестановка точек ромбом не является
        return 0

    best_points = []
    best_square = 0
    combinations = comb(n, 4)  # все возможные комбинации 4х точек из n
    for c in combinations:  # перебираем текущую комбинацию
        cur_combination = [points[i-1] for i in c]  # точки текущей комбинации
        cur_square = rhomb_square(cur_combination)  # площадь текущей комбинации точек
        if cur_square > best_square:  # если площадь больше текущей максимальной, то предыдущие ромбы не нужны
            best_square = cur_square
            best_points.clear()
        if cur_square == best_square:  # если площадь ромба равна максимальной, то добавляем его в лучшие ромбы
            best_points.append(cur_combination)
    return best_square, best_points


if __name__ == '__main__':

    n = int(input("Введите количество точек и сами точки:\n"))
    points = []

    for _ in range(n):
        points.append(tuple(map(int, input().split())))

    rhombs = solve_rhomb() if n > 3 else (0, 0)

    if rhombs[0]:
        print("Максимальная площадь ромба:", rhombs[0])
        print("Комбинации точек, из которых может получится данный ромб:")
        for points in rhombs[1]:
            print(points)
    else:
        print("Нет ни одного ромба")