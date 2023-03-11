def hamming(x,y):
    distance = 0
    for a,b in zip(x,y):
        if a != b:
            distance += 1
    return distance

x = list(map(int,input().split()))
y = list(map(int,input().split()))
print(hamming(x,y))