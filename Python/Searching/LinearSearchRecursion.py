def linear_search(arr,low,high,x):
    if high >= low:
        if arr[low] == x:
            return low
        elif arr[high] == x:
            return high
        else:
            return linear_search(arr,low+1,high-1,x)
    else:
        return -1
    
arr = list(map(int, input("Enter Arrar: ").split())
x = int(input())

result = linear_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
