def binarySearch(arr,start,end,key):
    mid = (start + end) // 2
    if start <= end:
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            binarySearch(arr,mid+1,end,key)
        else:
            binarySearch(arr,start,mid-1,key)
    else:
        return -1
        

arr = list(map(int, input("Enter Arrar: ").split()))
key = int(input())
l = len(arr)-1
result = binarySearch(arr,0,l,key)
if (result == -1):
    print("Element not Found!!!")
else:
    print("element is present at position: ",result)
