

# github.com/HigerSkill
def combinations(n, k):
    A = []
    B = [i+1 for i in range(k)]

    if n == k:
        return [B]
    elif n < k or not k:
        return []

    p = k
    while p >= 0:
        A.append(B.copy())
        p = p-1 if B[k-1] == n else k-1
        if p >= 0:
            for i in range(k-1, p-1, -1):
                B[i] = B[p] + i - p + 1

    return A


# github.com/HigerSkill
def permutations(n):
    A = []
    B = [i+1 for i in range(n)]

    if n == 0:
        return [[0]]
    elif n < 0:
        return []

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


def accommodations(n, k):
    permuts = permutations(k)  # все возможные перестановки к чисел
    combs = combinations(n, k)  # все возможные выборки из n по k
    all_vectors = []
    for vector in combs:  # для каждой выборки
        for permut in permuts:  # смотрим все ее перестановки и добавляем к ответу
            new_vector = [vector[permut[i]-1] for i in range(k)]
            all_vectors.append(new_vector)
    return all_vectors


def solve_rhomb():
    from math import sqrt
    get_len_sqr = lambda p1, p2: (p1[0]-p2[0])**2+(p1[1]-p2[1])**2  # квадрат расстояния между точками p1, p2
    scalar_product = lambda v1, v2: v1[0]*v2[0] + v1[1]*v2[1]  # скалярное произведение
    permuts = permutations(4)

    def rhomb_square(cur_points):
        for permut in permuts:
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
    combs = combinations(n, 4)  # все возможные комбинации 4х точек из n
    for c in combs:  # перебираем текущую комбинацию
        cur_combination = [points[i-1] for i in c]  # точки текущей комбинации
        cur_square = rhomb_square(cur_combination)  # площадь текущей комбинации точек
        if cur_square > best_square:  # если площадь больше текущей максимальной, то предыдущие ромбы не нужны
            best_square = cur_square
            best_points.clear()
        if cur_square == best_square:  # если площадь ромба равна максимальной, то добавляем его в лучшие ромбы
            best_points.append(cur_combination)
    return best_square, best_points


# github.com/HigerSkill
def S(P, c, v):
    n = len(c[0])
    s = 0
    for i in range(n):
        for j in range(n):
            s += c[i][j] * v[P[i]-1][P[j]-1]

    return s


# github.com/HigerSkill
def appoint(c, v, a):
    n = len(a[0])
    p = permutations(n)

    found = []
    variant = []
    ind = []

    for i in range(len(p)):
        ok = 0
        for j in range(n):
            search = p[i]
            l = search[j]
            if a[j][l - 1] == 0:
                ok += 1
        if ok == n:
            found.append(p[i])

    for i in range(len(found)):
        variant.append(S(found[i], c, v))

    if not variant:
        return []

    varmin = min(variant)
    for i in range(len(variant)):
        if variant[i] == varmin:
            ind.append(i)

    ans = [found[ind[i]] for i in range(len(ind))]
    return ans


if __name__ == '__main__':
    """
    print(combinations(1, 0))
    print(accommodations(1, 0))
    print(combinations(1, 1))
    print(accommodations(1, 1))
    print(combinations(0, 1))
    print(accommodations(0, 1))
    print(combinations(3, 3))
    print(accommodations(3, 3))
    print(combinations(3, 2))
    print(accommodations(3, 2))
    print(combinations(2, 3))
    print(accommodations(2, 3))
    print(combinations(4, 3))
    print(accommodations(4, 3))
    """
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

    print("Квадратичная задача о назначениях")
    n = int(input("Введите количество городов: "))
    print("введите матрицу цен:")
    C = [list(map(int, input().split())) for _ in range(n)]
    print("введите матрицу объемов перевозок:")
    V = [list(map(int, input().split())) for _ in range(n)]
    print("введите матрицу запрещенных назначений:")
    A = [list(map(int, input().split())) for _ in range(n)]
    print(appoint(C, V, A))
