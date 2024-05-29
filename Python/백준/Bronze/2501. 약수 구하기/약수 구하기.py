n, k = map(int, input().split())
res = []

for num in range(1, n + 1):
    if n % num == 0:
        res.append(num)

if k <= len(res):
    print(res[k - 1]) 
else:
    print(0)  
