def QuickSort(A,low,high):
    if low < high:
        p = Partition(A,low,high)
        QuickSort(A,low,p-1)
        QuickSort(A,p+1,high)

def Partition(A,low,high):

    pivot = A[high]
    i = low-1
    for j in range(low,high):
        if A[j] < pivot:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[high] = A[high],A[i+1]
    return i+1

A = list(map(int,input().split()))
QuickSort(A,0,len(A)-1)
print(A)

