res = []
for _ in range(10):
    n = int(input())
    x = n % 42
    if x not in res:
        res.append(x)
print(len(res))