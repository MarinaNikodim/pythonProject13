#from itertools import combinations

def Findpairs(targ_value, m_2nd_tablo):
    m_2nd_tablo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    result = {}
    for target in targ_value:
        pairs = []
        for i in range(len(m_2nd_tablo)):
            for j in range(i +1, len(m_2nd_tablo)):
                if m_2nd_tablo[i] + m_2nd_tablo[j] == target:
                    pairs.append((m_2nd_tablo[i], m_2nd_tablo[j]))
        result[target] = pairs
    return result

def filter_multiples(n, lst):
    return [x for x in lst if x % n == 0]


n_1st_tablo = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
m_2nd_tablo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
filtered_m_2nd_tablo = filter_multiples(n_1st_tablo[0], m_2nd_tablo)
result = Findpairs(n_1st_tablo, filtered_m_2nd_tablo)
for target, pairs in result.items():
    print(f"пары для числа: {target}- {pairs}")
