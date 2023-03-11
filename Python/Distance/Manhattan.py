def manhattan(x,y):
    distance = 0
    for a,b in zip(x,y):
        distance += abs(a-b)
    return distance

x = list(map(int,input().split()))
y = list(map(int,input().split()))
print(manhattan(x,y))