def SelectionSort(A):
    for i in range(len(A)):
        min = i
        for j in range(i+1,len(A)):
            if A[j]<A[min]:
                min = j
        A[i],A[min]=A[min],A[i]
    return A

A = list(map(int, input().split()))

print(SelectionSort(A))
