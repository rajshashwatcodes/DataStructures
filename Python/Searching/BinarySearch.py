def binarySearch(arr,key):
    start = 0
    end = len(arr)-1

    
    while(start<=end):
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1
  
arr = list(map(int, input().split()))
k = int(input())
result = binarySearch(arr,k)
if result == -1:
    print("Element not found!")
else:
    print("Element present at index: ", result)
