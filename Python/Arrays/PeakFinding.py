def find_element(arr, low, high):
    if low > high:
        return None

    mid = (low + high) // 2

    if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
        return arr[mid]
    
    if mid > 0 and arr[mid - 1] > arr[mid]:
        return find_element(arr, low, mid - 1)
    else:
        return find_element(arr, mid + 1, high)


array1 = [1, 2, 3, 4, 5]
result1 = find_element(array1, 0, len(array1) - 1)
print(result1)  
