import math

def eculidean(x,y):
    distance = 0
    for a,b in zip(x,y):
        distance += pow((a-b),2)
    return math.sqrt(distance)

x = list(map(int,input().split()))
y = list(map(int,input().split()))
print(eculidean(x,y))
