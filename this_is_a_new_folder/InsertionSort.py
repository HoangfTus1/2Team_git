sorting_array = [12, 33, 13, 66, 89, 10, 23, 57, 80]

n = len(sorting_array)
for i in range(1 , n):
    insert_index = i
    current_value = sorting_array[i]
    for j in range(i - 1, -1, -1):
        if sorting_array[j] > current_value:
            sorting_array[j + 1] = sorting_array[j]
            insert_index = j
        else:
            break
    sorting_array[insert_index] = current_value

print("Sorted array:", sorting_array)