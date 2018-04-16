
def haffman(p, k, C, L):
    if k <= 2:
        try:
            C[0] = '0'
            L[0] = 1
            C[1] = '1'
            L[1] = 1
        except:
            pass
        finally:
            return
    d = p[-1] + p[-2]
    j = insert(p, k, d)
    haffman(p[:-1], k-1, C, L)
    down(k, j, C, L)


def down(k, j, C, L):
    b = C[j]
    l = L[j]
    for i in range(j, k-1):
        C[i] = C[i+1]
        L[i] = L[i+1]
    C[k-2] = b + '0'
    C[k-1] = b + '1'
    L[k-2] = L[k-1] = l+1


def insert(p, k, d):
    j = k-2
    p[j] = d
    while j and p[j-1] < p[j]:
        p[j], p[j - 1] = p[j - 1], p[j]
        j -= 1
    return j


def test(P):
    scalar_product = lambda x, y: sum([x[i] * y[i] for i in range(len(x))])
    n = len(P)
    C = ['' for _ in range(n)]
    L = [0 for _ in range(n)]
    haffman(P.copy(), n, C, L)
    print("набор вероятностей: ", P)
    print("Оптимальные коды:\n", C)
    print("Lсредняя =", scalar_product(L, P))
    return P, C, scalar_product(L, P)

if __name__ == '__main__':
    """
    # тест
    P = [0.22, 0.2, 0.16, 0.16, 0.1, 0.1, 0.04, 0.02]
    n = len(P)
    C = ['' for _ in range(n)]
    L = [0 for _ in range(n)]
    haffman(P.copy(), n)
    print(P)
    print(L)
    print(C)
    scalar_product = lambda x, y: sum([x[i]*y[i] for i in range(len(x))])
    print(scalar_product(L, P))
    """
    P = [0.21, 0.2, 0.17, 0.16, 0.12, 0.08, 0.04, 0.02]
    test(P)
    P = [0.5, 0.2, 0.1, 0.09, 0.08, 0.03]
    test(P)


    text = "и_сердце_бьется_в_упоенье,_" \
           "и_для_него_воскресли_вновь_" \
           "и_божество,_и_вдохновенье,_" \
           "и_жизнь,_и_слезы,_и_любовь."
    text = input("Введите текст:\n")
    m = len(text)
    print("длина текста:", m)
    alph = {}
    for c in text:
        alph[c] = 1 + alph.get(c, 0)
    print("алфавит: ", list(alph.keys()))

    freq_smb = {}  # частота -> набор символов
    smb_freq = {}  # символ -> частота
    p = []
    used = set()
    for c in text:
        if not c in used:
            tmp = alph[c]/m
            p.append(tmp)
            smb_freq[c] = tmp
            freq_smb[tmp] = freq_smb.get(tmp, set()).union(set(c))
            used.add(c)

    p.sort(key=lambda x: -x)
    used.clear()
    print("частоты в порядке убывания:\n")
    for e in p:
        if not e in used:
            print(e, ':', freq_smb[e])
            used.add(e)

    optimum_code, l_avg = test(p)[1:]

    coded_text = ""

    for c in text:
        coded_text += optimum_code[p.index(smb_freq[c])]
    newm = len(coded_text)
    print("Длина закодированного текста: ", newm, ", текст:", sep='')
    print(coded_text)
    print("коэффициент сжатия:", (8-l_avg)/8*100, '%')
