tablo1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tablo2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

def find_pairs(tablo1, tablo2):
    result = {}
    for num in tablo1:
        pairs = []
        for i in range(len(tablo2)):
            for j in range(i + 1, len(tablo2)):
                if num % (tablo2[i] + tablo2[j]) == 0:
                    pairs.append((tablo2[i], tablo2[j]))
        result[num] = pairs
    return result


result_total = find_pairs(tablo1, tablo2)

for num, pairs in result_total.items():
    print(f"Пары для числа {num} - {pairs}")