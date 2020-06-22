def search_pairs(array, k):
    new_array = []
    n = 0
    len_array = len(array)
    for i in range(0, len_array - n):
        for j in range(i + 1, len_array - n):
            if array[i + n] + array[j + n] == k:
                now = sorted([array[i + n], array[j + n]])
                if now not in new_array:
                    new_array.append(now)
    return new_array


# Сложность небольшая, но как оптимизировать этот код не знаю,
# т.к. попытался сделать это сам на сколько могу.