sorting_array = [12, 7, 4, 15, 34, 16]

n = len(sorting_array)
for i in range(n - 1):
    swapping = False
    for j in range(n - i - 1):
        if sorting_array[j] > sorting_array[j + 1]:
            sorting_array[j], sorting_array[j + 1] = sorting_array[j + 1], sorting_array[j]
            swapping = True
    if not swapping:
        break

print("Sorted Array:", sorting_array)