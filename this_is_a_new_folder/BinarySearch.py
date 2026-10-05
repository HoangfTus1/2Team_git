def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        
        else:
            right = mid - 1
    return -1

sortedArr = [1, 2, 12, 13, 15, 17, 21, 27, 38, 40]
Targeted = 2

result = binarySearch(sortedArr, Targeted)

if result != -1:
    print("Value", Targeted,"Found at index:", result)
else:
    print("Value", Targeted,"Not found")