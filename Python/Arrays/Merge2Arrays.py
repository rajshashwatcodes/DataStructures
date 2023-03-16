a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
i = 0
j = 0
while i < len(a)-1 or j < len(b)-1:
    if a[i] < b[j] and i < len(a)-1:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
print(c)

