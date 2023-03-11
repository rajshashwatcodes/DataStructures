def chebyshev(x,y):
    distance = 0
    for a,b in zip(x,y):
        distance.append(abs(a-b))
    return(max(distance))

x = list(map(int,input().split()))
y = list(map(int,input().split()))
print(chebyshev(x,y))