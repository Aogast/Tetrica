def search_pairs(array, k):
    new_array = []
    len_array = len(array)
    for i in range(0, len_array):
        for j in range(i + 1, len_array):
            if array[i] + array[j] == k:
                now = sorted([array[i], array[j]])
                if now not in new_array:
                    new_array.append(now)
    return new_array


print(search_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))


# Сложность небольшая, но как оптимизировать этот код не знаю,
# т.к. попытался сделать это сам на сколько могу.