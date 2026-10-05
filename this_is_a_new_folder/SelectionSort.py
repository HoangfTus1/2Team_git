sorting_array = [45, 4, 1, 12, 33, 99, 156, 48, 65]

n = len(sorting_array)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if sorting_array[j] < sorting_array[min_index]:
            min_index = j
    sorting_array[i], sorting_array[min_index] = sorting_array[min_index], sorting_array[i]

print("Sorted array:", sorting_array)