def countingSort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    arr[:] = []
    for num, freq in enumerate(count):
        arr.extend([num] * freq)
        
    return arr

unsortedArr = [4, 2, 1, 4, 2, 6, 5, 7, 1, 8, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)