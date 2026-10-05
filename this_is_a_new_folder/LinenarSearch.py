def linenarSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr = [3, 7, 11, 5, 6, 2, 79, 88]
targetVal = 3

result = linenarSearch(arr, targetVal)

if result != -1:
    print("Target", targetVal,"Found at index:", result)
else:
    print("Target", targetVal, "Not found")