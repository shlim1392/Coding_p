chess = list(map(int, input().split()))
keep = [1, 1, 2, 2, 2, 8]
res = []
for i in range(6):
    a = keep[i] - chess[i]
    res.append(a)
print(' '.join(map(str, res)))