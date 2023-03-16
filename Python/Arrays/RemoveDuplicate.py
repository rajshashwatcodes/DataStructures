n = list(map(int,input().split()))
f = []
print(f)
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        f.append(n[i])
f.append(n[-1])
print(f)
